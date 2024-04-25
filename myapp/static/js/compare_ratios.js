document.addEventListener("DOMContentLoaded", function() {
    var companySelect = document.getElementById("company");
    var year1Select = document.getElementById("year1");
    var year2Select = document.getElementById("year2");

    companySelect.addEventListener("change", function() {
        var selectedCompany = companySelect.value;

        year1Select.innerHTML = '<option value="" disabled selected hidden>Year 1</option>';
        year2Select.innerHTML = '<option value="" disabled selected hidden>Year 2</option>';

        var selectedCompanyData = companyData.find(function(item) {
            return item.company === selectedCompany;
        });

        if (selectedCompanyData && selectedCompanyData.Dates) {
            selectedCompanyData.Dates.forEach(function(year) {
                var option1 = document.createElement("option");
                var option2 = document.createElement("option");
                option1.value = year;
                option1.text = year;
                option2.value = year;
                option2.text = year;

                if (year !== year1Select.value) {
                    year1Select.appendChild(option1);
                }
                if (year !== year2Select.value) {
                    year2Select.appendChild(option2);
                }
            });
        }
    });

    year1Select.addEventListener("change", function() {
        var selectedYear = year1Select.value;
        for (var i = 0; i < year2Select.options.length; i++) {
            if (year2Select.options[i].value === selectedYear) {
                year2Select.remove(i);
                break;
            }
        }
    });

    year2Select.addEventListener("change", function() {
        var selectedYear = year2Select.value;
        for (var i = 0; i < year1Select.options.length; i++) {
            if (year1Select.options[i].value === selectedYear) {
                year1Select.remove(i);
                break;
            }
        }
    });
});
