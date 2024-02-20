var form = document.getElementById('leave-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    var selectedOption = document.querySelector('#user-list option[value="' + formData.get('employee_id') + '"]');
    var userId = selectedOption.getAttribute('data-value');
    formData.set('employee_id', userId)
    $.ajax({
        type: 'POST',
        url: '/save-leave/',
        data: formData,
        processData: false,
        contentType: false,
        xhrFields: {
            withCredentials: true
        },
        success: function (response) {
            if (response.success) {
                alert('Saved successfully');
            } else {
                alert(response.message);
            }
        },
        error: function (error) {
            console.log(error);
            alert('An error occurred. Please try again.');
        }
    });
});

function isSunday(date) {
    return date.getDay() === 0; // 0 corresponds to Sunday
}

// Show warning if selected date or date range includes a Sunday
function checkForSunday() {
    var today = new Date();
    var startDateInput = document.getElementById('start_date');
    var endDateInput = document.getElementById('end_date');
    var startDate = new Date(startDateInput.value);
    var endDate = new Date(endDateInput.value);

    if (todayRadio.checked && isSunday(today)) {
        Swal.fire({
            title: "Warning",
            text: "It's a Sunday. Please review.",
            icon: "warning",
            button: "OK",
        });
    } else if (dateRangeRadio.checked) {
        var current = new Date(startDate);
        while (current <= endDate) {
            if (isSunday(current)) {
                Swal.fire({
                    title: "Warning",
                    text: "Selected date range includes a Sunday. Please review.",
                    icon: "warning",
                    button: "OK",
                });
                break;
            }
            current.setDate(current.getDate() + 1);
        }
    }
}

// Show/hide date range fields based on date option
var todayRadio = document.getElementById('today');
var dateRangeRadio = document.getElementById('date_range');
var dateRangeFields = document.getElementById('date-range-fields');

function showDateRangeFields() {
    dateRangeFields.style.display = 'block';
}

function hideDateRangeFields() {
    dateRangeFields.style.display = 'none';
}

function handleDateOptionChange() {
    if (dateRangeRadio.checked) {
        showDateRangeFields();
        checkForSunday();
    } else {
        hideDateRangeFields();
    }
}

todayRadio.addEventListener('change', function() {
    if (todayRadio.checked) {
        hideDateRangeFields();
        checkForSunday();
    }
});

dateRangeRadio.addEventListener('change', handleDateOptionChange);

// Event listeners for date inputs to check for Sunday
document.getElementById('start_date').addEventListener('change', checkForSunday);
document.getElementById('end_date').addEventListener('change', checkForSunday);

// Initial check for date option and date inputs on page load
handleDateOptionChange();
checkForSunday();
