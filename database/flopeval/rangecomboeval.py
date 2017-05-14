import psycopg2
import logging
from psycopg2.extras import LoggingConnection

from flopevaluator import FlopEvaluator, prettify_eval_results
from rangeparser import hand_range_to_cards, card_ints_to_str
from canonflop import canon
from constants import HANDS, HANDS_VALUE

from collections import defaultdict

def name_replace(s):
    return s.replace(' ', '_')\
            .replace(':', '')\
            .replace(',', '')\
            .lower()

sql_statements = {
    "create ranges table": """
CREATE TABLE IF NOT EXISTS ranges (
id SERIAL PRIMARY KEY NOT NULL,
range_label TEXT,
range_desc TEXT
)
""",
    "create combohashes table":
        """CREATE TABLE IF NOT EXISTS combohashes (
            rangeid INTEGER NOT NULL,
            flop TEXT,
            %s
            FOREIGN KEY(rangeid) REFERENCES ranges,
            PRIMARY KEY (rangeid, flop)
           )
        """ % ''.join(["%s INTEGER, " % name_replace(s) for s in HANDS]),
    "insert ranges": "INSERT INTO ranges (range_label, range_desc) VALUES (%(range_label)s, %(range_desc)s) RETURNING id",
    "insert combohashes":
        "INSERT INTO combohashes (rangeid, flop, %s) " % ', '.join(["%s" % name_replace(s) for s in HANDS]) +
        "VALUES (%(rangeid)s, %(flop)s, " + "%s)" % ', '.join(["%(" + s + ")s" for s in HANDS]),
    "select combohashes flop":
        "SELECT * FROM combohashes WHERE combohashes.rangeid='%s' AND combohashes.flop='%s'",
    "select combohashes anyflop": "SELECT * FROM combohashes WHERE combohashes.rangeid='%s'",
    "select ranges id by label": "SELECT id FROM ranges WHERE range_label='%s'",
}

class RangeComboEvaluator:
    def __init__(self):
        self._connect()

    def _connect(self):
        #logging.basicConfig(level=logging.DEBUG)
        #logger = logging.getLogger(__name__)
        #self.conn = psycopg2.connect("", connection_factory=LoggingConnection)
        #self.conn.initialize(logger)
        self.conn = psycopg2.connect("")
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql_statements['create ranges table'])
        self.cursor.execute(sql_statements['create combohashes table'])
        self.conn.commit()

    def evaluate_flops_for_range(self, flops, range, rangename):
        cursor = self.cursor
        cursor.execute(sql_statements["select ranges id by label"] % rangename)
        result = cursor.fetchall()
        if len(result) == 0:
            cursor.execute(sql_statements["insert ranges"], {'range_label': rangename, 'range_desc': range})
            rangeid = cursor.fetchone()[0]
        elif len(result) == 1:
            rangeid = result[0][0]
        for flop in flops:
            canonflop = list(canon(flop))
            cursor.execute(sql_statements["select combohashes flop"] % (rangeid, card_ints_to_str(canonflop)))
            if len(cursor.fetchall()) > 0:
                continue
            hands = hand_range_to_cards(range, canonflop)
            if len(hands) == 0:
                continue
            combohash = defaultdict(lambda: 0)
            combohash.update(prettify_eval_results(FlopEvaluator.evaluate_for_range(canonflop, hands)))
            combohash.update({'rangeid': rangeid, 'flop': card_ints_to_str(canonflop)})
            cursor.execute(sql_statements["insert combohashes"], combohash)
        self.conn.commit()

    def get_combohashes_for_range(self, rangename):
        cursor = self.cursor
        cursor.execute(sql_statements["select ranges id by label"] % rangename)
        rangeid = cursor.fetchall()[0][0]
        cursor.execute(sql_statements["select combohashes anyflop"] % rangeid)
        results = cursor.fetchall()
        combohashes = []
        for result in results:
            combohash = {}
            for i, hand_count in enumerate(result[2:]):
                if hand_count:
                    combohash[i] = hand_count
            combohashes.append(combohash)
        return combohashes

if __name__ == '__main__':
    from itertools import combinations

    btn = "22+,A2s+,K2s+,Q2s+,J6s+,T6s+,96s+,86s+,75s+,64s+,53s+,43s,32s,A2o+,K8o+,Q8o+,J8o+,T8o+,98o,87o"
    utg = "77+,ATs+,KTs+,QTs+,JTs,T9s,AJo+,KQo"

    canon_flops = []
    for flop in combinations(range(52), 3):
        canon_flops.append(canon(flop))
    deduped_flops = sorted(list(set(canon_flops)))

    rceval = RangeComboEvaluator()
    rceval.evaluate_flops_for_range(deduped_flops, utg, 'utg')
    rceval.evaluate_flops_for_range(deduped_flops, btn, 'btn')
    rceval.evaluate_flops_for_range(deduped_flops, utg, 'utg')
    rceval.evaluate_flops_for_range(deduped_flops, btn, 'btn')

