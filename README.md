# airwave-python
Python examples for Aruba AirWave

Demonstrating the "old" way of obtaining information from the Airwave XML API (which still works at time of writing!) and the "new" way involving cookies and X-BISCOTTI and all that jazz.

The "old" way just sends the login credentials with every request.

The "new" way is as-documented in the AirWave 8.2.15.0 API Guide. It requires you to make at least two requests. The first is a request to log in, and you must save the cookies that were created in that request along with a special header value that is returned called "X-BISCOTTI" . The cookies and the "X-BISCOTTI" header can be used as "tokens" for future requests, without re-sending the credentials themselves. You could make several requests using theses "tokens" without re-sending the actual credentials.

Note that in the "new" way we wrap the first request inside a session so we can examine the cookies that are returned.

We could reasonably expect the "old" way to stop working at some future release, so should probably migrate to the "new" way where possible.
