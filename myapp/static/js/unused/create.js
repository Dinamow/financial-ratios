// create.js

function validateForm() {
  var inputs = document.getElementsByTagName("input");
  for (var i = 0; i < inputs.length; i++) {
    var input = inputs[i];
    var value = input.value.trim();
    if (value === "" || value.startsWith("0") || !/^\d+(\.\d+)?$/.test(value)) {
      alert(
        "Please fill in all fields with valid numeric values that do not start with 0."
      );
      return false;
    }
  }
  return true;
}

document.addEventListener("DOMContentLoaded", function () {
  var submitBtn = document.getElementById("submit-btn");
  submitBtn.disabled = true; // initially disable the button
  var inputs = document.getElementsByTagName("input");
  for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener("input", function () {
      var allFilled = true;
      for (var j = 0; j < inputs.length; j++) {
        if (
          inputs[j].id === "submit-btn" ||
          inputs[j].name === "csrfmiddlewaretoken"
        )
          continue;
        if (inputs[j].name === "company") {
          if (
            inputs[j].value.trim() === "" ||
            inputs[j].value.length > 50 ||
            !/^[a-zA-Z\s]+$/.test(inputs[j].value)
          ) {
            allFilled = false;
            break;
          }
        } else if (inputs[j].name === "year") {
					if (
						inputs[j].value.trim() === "" ||
						inputs[j].value.length !== 4 ||
						!/^\d+$/.test(inputs[j].value)
					) {
						allFilled = false;
						break;
					}
				}
				 else if (
          inputs[j].value.trim() === "" ||
          inputs[j].value.startsWith("0") ||
          !/^\d+(\.\d+)?$/.test(inputs[j].value)
        ) {
          allFilled = false;
          break;
        }
      }
      submitBtn.disabled = !allFilled;
    });
  }
});
