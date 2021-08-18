let body = document.getElementsByTagName('body')[0];

function getTime(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", '/current_time/', false);
    xmlHttp.send(null);
    return JSON.parse(xmlHttp.responseText)['current_time'];
}

setInterval(() => {
    body.innerText = `Current time: ${getTime()}`
}, 1000)


