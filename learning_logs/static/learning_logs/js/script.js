$(document).ready(function () {
  // Add interactivity here
  $("nav ul li a").on("click", function () {
    alert("Navigating to " + $(this).text());
  });
});
