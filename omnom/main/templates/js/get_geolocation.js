
$(document).ready(function() {


    navigator.geolocation.getCurrentPosition(
	function(data) {
	    var latitude = data.coords.latitude;
	    var longitude = data.coords.longitude;

	    $('#request-form input[name=latitude]').val(latitude);
	    $('#request-form input[name=longitude]').val(longitude);
	}
    );


});
