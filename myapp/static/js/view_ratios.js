document.addEventListener("DOMContentLoaded", function() {
    var companySelect = document.getElementById("company");
    var yearSelect = document.getElementById("year");
    var resultsElement = document.querySelector(".results");

    var urlSearchParams = new URLSearchParams(window.location.search);
    var hasParameters = urlSearchParams.has('company');

    if (!hasParameters) {
        resultsElement.style.display = "none";
    }

    companySelect.addEventListener("change", function() {
        var selectedCompany = companySelect.value;

        yearSelect.innerHTML = '<option value="" disabled selected hidden>Year</option>';

        var selectedCompanyData = companyData.find(function(item) {
            return item.company === selectedCompany;
        });

        if (selectedCompanyData && selectedCompanyData.Dates) {
            selectedCompanyData.Dates.forEach(function(year) {
                var option = document.createElement("option");
                option.value = year;
                option.text = year;
                yearSelect.appendChild(option);
            });
        }
    });
});
