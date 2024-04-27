document.addEventListener("DOMContentLoaded", function() {
    var companySelect = document.getElementById("company");
    var year1Select = document.getElementById("year1");
    var year2Select = document.getElementById("year2");
    var resultsElement = document.querySelector(".results");
    var loadingElement = document.querySelector(".loading");

    var urlSearchParams = new URLSearchParams(window.location.search);
    var hasParameters = urlSearchParams.has('company');

    if (!hasParameters) {
        resultsElement.style.display = "none";
    } else {
        loadingElement.style.display = "none";
    }

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

function showPopup(formula1, numbers1, formula2, numbers2, value1, value2, status1, status2) {
    var popup = document.querySelector('.popup');
    var overlay = document.querySelector('.popup-overlay');

    var tableBody = popup.querySelector('tbody');
    tableBody.innerHTML = `
        <tr>
            <td>Formula</td>
            <td>${formula1}</td>
            <td>${formula2}</td>
        </tr>
        <tr>
            <td>Numbers</td>
            <td>${numbers1}</td>
            <td>${numbers2}</td>
        </tr>
        <tr>
            <td>Values</td>
            <td class="${status1}">${value1}</td>
            <td class="${status2}">${value2}</td>
        </tr>
    `;

    popup.style.display = 'block';
    overlay.style.display = 'block';
}

function closePopup() {
    var popup = document.querySelector('.popup');
    var overlay = document.querySelector('.popup-overlay');
    popup.style.display = 'none';
    overlay.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    var overlay = document.querySelector('.popup-overlay');

    overlay.addEventListener('click', function() {
        closePopup();
    });
});