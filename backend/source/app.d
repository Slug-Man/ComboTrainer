import vibe.vibe;
import std.process;

void main()
{
	auto ip = executeShell("hostname -i");
	auto settings = new HTTPServerSettings;
	settings.port = 8080;
	settings.bindAddresses = [ip.output.chomp];
	listenHTTP(settings, &hello);

	logInfo("Please open http://%s:8080/ in your browser.".format(ip.output.chomp));
	runApplication();
}

void hello(HTTPServerRequest req, HTTPServerResponse res)
{
	res.writeBody("Hello, World!");
}
