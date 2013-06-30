
$(document).ready(function() {
    init()
});

function init() {    
    navigator.geolocation.getCurrentPosition(
	function(data) {
	    var latitude = data.coords.latitude;
	    var longitude = data.coords.longitude;

	    $('#request-form input[name=latitude]').val(latitude);
	    $('#request-form input[name=longitude]').val(longitude);
	}
    );
}
