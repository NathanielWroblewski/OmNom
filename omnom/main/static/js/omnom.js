
$(document).on("pageinit",function(event) {init()});

function drawMap(container,overrideOptions,callback) {
  if(typeof(overrideOptions)==='undefined') overrideOptions = {};
  if (!navigator.geolocation) {
    return;
  }
  /* By default, maps will be drawn such that the center is your location */
  navigator.geolocation.getCurrentPosition(function(position){

    var latlng = new google.maps.LatLng(position.coords.latitude,
      position.coords.longitude);
    var myOptions = {
      zoom: 8,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    for (key in overrideOptions) {
      if (overrideOptions.hasOwnProperty(key)) {
        myOptions[key] = overrideOptions[key]
      }
    }

    var map = new google.maps.Map(container,myOptions);
    return callback(map);
  });

}

function init() {
  $('#request-form').each(function(i,e) {
    console.log("hello");
    if(navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position){
        $('input[name=latitude]',e).val(position.coords.latitude);
        $('input[name=longitude]',e).val(position.coords.longitude);
      });
    }
  });

  $('#donation-map').each(function(i,e) {
    drawMap(e,{},function(map) {
      var markerData = $(e).data("markers") || [];
      $(markerData).each(
        function(index,markerElement) {
          a = map;
          var latlng = new google.maps.LatLng(markerElement[0],
            markerElement[1]);
          var marker = new google.maps.Marker({
            position: latlng,
            map: map,
            icon: "/static/css/images/blackmarker.png",
            title: 'Hello World!'
          });
          var infoWindow = new google.maps.InfoWindow({
          content: "<a href='/messenger/confirmation/" + markerElement[3] + "'>"+ markerElement[4] +"</a>" + "<br> Donation posted at:" +markerElement[2]
          });

          google.maps.event.addListener(marker, 'click', function(){
            infoWindow.open(map, marker);
          });
        }
        );

    });


  });
}
