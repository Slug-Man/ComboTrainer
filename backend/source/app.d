import vibe.vibe;
import std.process;

void main()
{
	auto ip = executeShell("hostname -i");

	auto settings = new HTTPServerSettings;
	settings.port = 8080;
	settings.bindAddresses = [ip.output.chomp];

	auto router = new URLRouter;
	router.get("/", &index);

	listenHTTP(settings, router);
	runApplication();
}

void index(HTTPServerRequest req, HTTPServerResponse res)
{
	res.render!("index.dt", req);
}
