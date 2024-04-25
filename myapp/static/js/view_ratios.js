document.addEventListener("DOMContentLoaded", function() {
    console.log("DOM loaded and parsed");
    console.log("Company data: ", companyData);
    var companySelect = document.getElementById("company");
    var yearSelect = document.getElementById("year");

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