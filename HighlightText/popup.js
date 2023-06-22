document.addEventListener("DOMContentLoaded", function() {
  const button = document.getElementById("button");
  const textField = document.getElementById("text-field");

  button.addEventListener("click", function() {
    // Get the value of the text field
    
    const text = textField.value;
      chrome.windows.create({
        url: chrome.runtime.getURL("mypage.html"),
        type: "popup"
      });

    // Update the popup with the text
    document.body.innerHTML = `<h3>${text}</h3>`;
  });
});