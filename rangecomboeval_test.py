from flopeval.rangecomboeval import *

if __name__ == '__main__':
    from itertools import combinations

    btn = "22+,A2s+,K2s+,Q2s+,J6s+,T6s+,96s+,86s+,75s+,64s+,53s+,43s,32s,A2o+,K8o+,Q8o+,J8o+,T8o+,98o,87o"
    utg = "77+,ATs+,KTs+,QTs+,JTs,T9s,AJo+,KQo"
    hj = "66+,A2s+,KTs+,QTs+,JTs,T9s,98s,ATo+,KJo+"
    co = "22+,A2s+,K8s+,Q9s+,J9s+,T8s+,97s+,87s,76s,65s,A9o+,KTo+,QTo+,JTo,T9o"
    sb = "22+,A2s+,K2s+,Q7s+,J7s+,T7s+,97s+,86s+,75s+,65s,54s,43s,A2o+,K9o+,Q9o+,J9o+,T8o+,98o"

    canon_flops = []
    for flop in combinations(range(52), 3):
        canon_flops.append(canon(flop))
    deduped_flops = sorted(list(set(canon_flops)))

    rceval = RangeComboEvaluator('./sqldb/rceval.db')
    rceval.evaluate_flops_for_range(deduped_flops, utg, 'utg')
    rceval.evaluate_flops_for_range(deduped_flops, hj, 'hj')
    rceval.evaluate_flops_for_range(deduped_flops, co, 'co')
    rceval.evaluate_flops_for_range(deduped_flops, btn, 'btn')
    rceval.evaluate_flops_for_range(deduped_flops, sb, 'sb')

    print 'utg', rceval.get_combohashes_for_range('utg')
    print 'hj', rceval.get_combohashes_for_range('hj')
    print 'co', rceval.get_combohashes_for_range('co')
    print 'btn', rceval.get_combohashes_for_range('btn')
    print 'sb', rceval.get_combohashes_for_range('sb')
