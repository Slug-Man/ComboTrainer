import std.process;
import std.string;

import vibe.core.core;
import vibe.core.log;
import vibe.http.router;
import vibe.http.server;
import vibe.web.rest;

import problemapi;

void main()
{
	auto router = new URLRouter;
    router.registerRestInterface(new ProblemAPI);

    auto ip = executeShell("hostname -i");
    auto settings = new HTTPServerSettings;
    settings.port = 8080;
    settings.bindAddresses = [ip.output.chomp];
    
	listenHTTP(settings, router);
    
	runApplication();	
	// create a client to talk to the API implementation over the REST interface
	/*runTask({
		auto client = new RestInterfaceClient!MyAPI("http://127.0.0.1:8080/");
		auto weather = client.getWeather();
		logInfo("Weather: %s, %s °C", weather.text, weather.temperature);
		client.location = "Paris";
		logInfo("Location: %s", client.location);
	});*/
}
