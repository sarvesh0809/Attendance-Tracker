var form = document.getElementById('employee-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    $.ajax({
        type: 'POST',
        url: '/create_employee/',
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
