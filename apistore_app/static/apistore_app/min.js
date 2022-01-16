       var myData = {
    hello: 1
};

fetch("/api/generate_bill/", {
    method: "get",
    credentials: "same-origin",
    headers: {
        "X-CSRFToken": getCookie("csrftoken"),
        "Accept": "application/json",
        "Content-Type": "application/json"
    },
    body: JSON.stringify(myData)
}).then(function(response) {
    return response.json();
}).then(function(data) {
    console.log("Data is ok", data);
}).catch(function(ex) {
    console.log("parsing failed", ex);
})
fetch()