$(document).ready( function() {
	$("#vehicle_form").hide();
	$("#z_pic").hide();
	$("#m_pic").hide();
	$("#s_pic").hide();
	$("#d_pic").hide();
	$("#open_sell").click( function(event) {
		$("#vehicle_form").slideToggle(500);
	});
	$("#zander").hover( function(event) {
		$("#z_pic").fadeIn(2000);
	});
	$("#deni").hover( function(event) {
		$("#d_pic").fadeIn(2000);
	});
	$("#sho").hover( function(event) {
		$("#s_pic").fadeIn(2000);
	});
	$("#micc").hover( function(event) {
		$("#m_pic").fadeIn(2000);
	});
	
	
});

