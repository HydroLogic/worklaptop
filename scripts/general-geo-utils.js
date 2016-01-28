var offsetPoint = function(p1,a,d){
    var brng = a*(Math.PI/180.0);
    var R = 41807040;
    var lat1 = (Math.PI/180.0)*p1.lat;
    var lon1 = (Math.PI/180.0)*p1.lng;
    var lat2 = Math.asin( Math.sin(lat1)*Math.cos(d/R) + 
            Math.cos(lat1)*Math.sin(d/R)*Math.cos(brng));
    var lon2 = lon1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(lat1), 
                     Math.cos(d/R)-Math.sin(lat1)*Math.sin(lat2));
    
    return {"lat":lat2*(180.0/Math.PI),"lng":lon2*(180.0/Math.PI)}
}
var bearing = function(p1,p2){
    var dLon = (Math.PI/180.0)*((p2.lng-p1.lng)),
        lat1 = (Math.PI/180.0)*p1.lat,
        lat2 = (Math.PI/180.0)*p2.lat,
        y = Math.sin(dLon) * Math.cos(lat2),
        x = Math.cos(lat1)*Math.sin(lat2) - Math.sin(lat1)*Math.cos(lat2)*Math.cos(dLon),
        brng = Math.atan2(y, x)*(180.0/Math.PI);
    return brng
}
var latLng2tile = function(lat,lon,zoom){
    var eLng = (lon+180)/360*Math.pow(2,zoom);
    var eLat = (1-Math.log(Math.tan(lat*Math.PI/180) + 1/Math.cos(lat*Math.PI/180))/Math.PI)/2 *Math.pow(2,zoom);
    //x coord in image tile of lat/lng
    var xInd = Math.round((eLng-Math.floor(eLng))*256);
    //y coord in image tile of lat/lng
    var yInd = Math.round((eLat-Math.floor(eLat))*256);
    //flattened index for clamped array in imagedata
    var fInd = yInd*256+xInd;
    //for calling tile from array
    var eLng = Math.floor(eLng);
    var eLat = Math.floor(eLat);
    return {"tileCall":""+zoom+"/"+eLng+"/"+eLat,"tileX":eLng,"tileY":eLat,"pX":xInd,"pY":yInd,"arrInd":fInd}
}
function drawChart(divID){
    var divH = document.getElementById(divID).clientHeight,
        divW = document.getElementById(divID).clientWidth,
        chartSRC = '<iframe src="chart.html" id="chartframe" frameborder=0 height="'+divH+'" width ="'+divW+'" scrolling="no"></iframe>';
        document.getElementById(divID).innerHTML = chartSRC;
}