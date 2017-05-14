import vibe.vibe;
import std.process;
import std.format;
import dpq2;

void main()
{
	auto ip = executeShell("hostname -i");

	auto settings = new HTTPServerSettings;
	settings.port = 8080;
	settings.bindAddresses = [ip.output.chomp];

	auto router = new URLRouter;
	router.get("/", &index);

	listenHTTP(settings, router);
	auto conn = new Connection("");
	auto result = conn.exec("select * from ranges where range_label='utg'");
	logInfo("utg range: %s".format(result[0]["range_desc"].as!PGtext));

	runApplication();
}

void index(HTTPServerRequest req, HTTPServerResponse res)
{
	res.render!("index.dt", req);
}
