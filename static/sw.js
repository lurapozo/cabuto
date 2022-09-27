var getTitle = function (title) {
    if (title === "") {
        title = "Nuevo pedido";
    }
    return title;
};

var getNotificationOptions = function (message, message_tag) {
    var options = {
        body: message,
        icon: 'https://cabutoshop.pythonanywhere.com/static/img/cabuto.png',
        tag: message_tag,
        vibrate: [200, 100, 200, 100, 200, 100, 200]
    };
    return options;
};

self.addEventListener('install', function (event) {
    self.skipWaiting();
});

self.addEventListener('push', function(event) {
    try {
        var response_json = event.data.json();
        var title = response_json.title;
        var message = response_json.message;
        var message_tag = response_json.tag;
    } catch (err) {
        var title = "";
        var message = event.data.text();
        var message_tag = "";
    }
    self.registration.showNotification(
      getTitle(title),
      getNotificationOptions(message, message_tag)
    );
    self.clients.matchAll({
        includeUncontrolled: true,
        type: 'window'
    }).then(function (clients) {
        clients.forEach(function (client) {
            client.postMessage({
                "data": message_tag,
                "data_title": title,
                "data_body": message
            });
        });
    });
});


self.addEventListener('notificationclick', function(event) {
    event.notification.close();
    event.waitUntil(clients.matchAll({
        type: 'window',
        includeUncontrolled: true
    }).then(function(windowClients){
        for (var i = 0; i < windowClients.length; i++) {
            var client = windowClients[i];
            if ('focus' in client) {
                return client.focus();
            }
        }
    }));
});