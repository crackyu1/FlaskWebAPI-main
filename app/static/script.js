document
  .getElementById("searchButton")
  .addEventListener("click", function (event) {
    event.preventDefault();
    var province = document.getElementById("province").value;
    var city = document.getElementById("city").value;
    debugger;
    if (province && city) {
      // Redirect to the weather page with the province and city as parameters
      var url = `http://127.0.0.1:5000/${encodeURIComponent(
        province
      )}/${encodeURIComponent(city)}`;
      window.location.href = url;
    } else {
      alert("Please enter both province and city names.");
    }
  });
