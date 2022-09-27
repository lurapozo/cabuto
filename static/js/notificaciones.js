function urlBase64ToUint8Array(base64String) {
    const padding = '='.repeat((4 - base64String.length % 4) % 4);
    const base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);
    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
}
function loadVersionBrowser (userAgent) {
        var ua = userAgent;
        var tem;
        var M = ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || [];if (/trident/i.test(M[1])) {
            tem = /\brv[ :]+(\d+)/g.exec(ua) || [];
            return {name: 'IE', version: (tem[1] || '')};
        }
        if (M[1] === 'Chrome') {
            tem = ua.match(/\bOPR\/(\d+)/);
            if (tem != null) {
                return {name: 'Opera', version: tem[1]};
            }
        }
        M = M[2] ? [M[1], M[2]] : [navigator.appName, navigator.appVersion, '-?'];
        if ((tem = ua.match(/version\/(\d+)/i)) != null) {
            M.splice(1, 1, tem[1]);
        }
        return {
            name: M[0],
            version: M[1]
        };
};
function requestPOSTToServer ( data ) {
    $.ajax({
        url: '/web_push/',
        data: {
            'browser': data.browser,
            'p256dh': data.p256dh,
            'auth': data.auth,
            'registration_id': data.registration_id
        },
        dataType: 'json',
        success: function (data) {
        }
      });
}
var applicationServerKey = "BFqmcBFK3lLHyynbBEiI51rhamk3kC4v_dtTCYtVtBBbMjoEoWvp3IycdVo5MiR0cocZ96k-zRaVwB07Lqhh24U";
if ('serviceWorker' in navigator) {
    var browser = loadVersionBrowser(navigator.userAgent);
    navigator.serviceWorker.register('/static/sw.js').then(function (reg) {
        reg.pushManager.subscribe({
            userVisibleOnly: true,
            applicationServerKey: urlBase64ToUint8Array(applicationServerKey)
        }).then(function (sub) {
            var endpointParts = sub.endpoint.split('/');
            var registration_id = endpointParts[endpointParts.length - 1];
            var data = {
                'browser': browser.name.toUpperCase(),
                'p256dh': btoa(String.fromCharCode.apply(null, new Uint8Array(sub.getKey('p256dh')))),
                'auth': btoa(String.fromCharCode.apply(null, new Uint8Array(sub.getKey('auth')))),
                'name': 'NUTONDIHI',
                'registration_id': registration_id
            };
            requestPOSTToServer(data);
        })
    }).catch(function (err) {
        if (Notification.permission === 'denied') {
            console.warn('Permission for notifications was denied');
        } else {
            console.error(':^(', err);
        }
    })
}