window.addEventListener("load", function () {
  function sendData() {
    var XHR = new XMLHttpRequest();

    // Bind the FormData object and the form element
    var FD = new FormData(form);
    var json_data = {
      "message":FD.get("message"),
      "emailAddress":FD.get("emailAddress")
    }

    // Define what happens on successful data submission
    XHR.addEventListener("load", function(event) {
      alert(event.target.response);
      window.location.replace("../contact_submit");
    });

    // Define what happens in case of error
    XHR.addEventListener("error", function(event) {
      alert('Oops! Something went wrong.');
    });

    // Set up our request
    XHR.open("POST", "https://oldmerkum-githubpage.prod.with-datafire.io/contact");
    XHR.setRequestHeader("Content-Type", "application/json");

    // The data sent is what the user provided in the form
    XHR.send(JSON.stringify(json_data));
    // Simulate an HTTP redirect:
  }

  // Access the form element...
  var form = document.getElementById("contact_form");

  // ...and take over its submit event.
  form.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
  });
});
