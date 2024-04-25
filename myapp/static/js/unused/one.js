window.onload = function() {
    const companySelect = document.getElementById('company');
    const yearSelect = document.getElementById('year');
    const companyData = JSON.parse(document.getElementById('company_data').textContent);

    companySelect.onchange = updateYears;

    function updateYears() {
        var selectedCompany = companySelect.value;

        // Clear previous options
        yearSelect.innerHTML = '<option value="" disabled selected hidden>Select year</option>';

        // Find the data for the selected company
        var selectedCompanyData;
        for (var i = 0; i < companyData.length; i++) {
            if (companyData[i].company === selectedCompany) {
                selectedCompanyData = companyData[i];
                break;
            }
        }

        // Populate years if data for the selected company exists
        if (selectedCompanyData && selectedCompanyData.Dates.length > 0) {
            for (var j = 0; j < selectedCompanyData.Dates.length; j++) {
                var option = document.createElement('option');
                option.text = selectedCompanyData.Dates[j];
                option.value = selectedCompanyData.Dates[j];
                yearSelect.appendChild(option);
            }
            yearSelect.disabled = false; // Enable the year select
        } else {
            // Disable the year select if no data available for the selected company
            yearSelect.disabled = true;
        }
    }
};
