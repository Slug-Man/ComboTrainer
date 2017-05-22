import vibe.vibe;
import vibe.web.rest;
import std.process;
import std.format;
import dpq2;

import problemapi;

void main()
{
	auto ip = executeShell("hostname -i");

	auto settings = new HTTPServerSettings;
	settings.port = 8080;
	settings.bindAddresses = [ip.output.chomp];

	auto router = new URLRouter;
	router.get("/", &index);
    router.registerRestInterface(new ProblemAPI);

	listenHTTP(settings, router);
    

	runApplication();
}

void index(HTTPServerRequest req, HTTPServerResponse res)
{
	res.render!("index.dt", req);
}
