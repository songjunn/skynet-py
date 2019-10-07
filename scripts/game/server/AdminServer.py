import skynet
import hotfix

def parser(url, args):
	p = url.split('?', 1)
	route = p[0]
	if len(p) > 1:
		t = p[1].split('&')
		for item in t:
			pos = item.index('=')
			k = item[0:pos]
			v = item[pos+1:]
			args[k] = v
	return route

def response(data):
	return 'HTTP/1.1 200 OK\r\n' + \
			  'Content-Type: text/plain\r\n' + \
			  'Content-Length: ' + str(len(data)) + '\r\n' + \
			  'Connection: keep-alive\r\n' + \
			  '\r\n' + data

def handleRequest(source, fd, url):
	skynet.logger_debug('[Game]recv http data: {}'.format(url))
	
	resp = ''
	args = {}
	route = parser(url, args)

	if route == '/gm/reload':
		resp = hotfix.reload()

	skynet.http_response_send(source, fd, response('success'))
