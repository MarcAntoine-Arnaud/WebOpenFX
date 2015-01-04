$(document).ready(function () {
	$("#render").click(function(){
		console.log("start rendering");

		$.ajax({
			type: "POST",
			url: "/render/",
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify({
				nodes: [{
					id: 0,
					plugin: "tuttle.colorwheel"
				},{
					id: 1,
					plugin: "tuttle.jpegwriter"
				}],
				connections: [{
						src : 0,
						dst: 1
				}],
				renderNode: 1
			})
		}).done(function(data){
			$("#viewer img").attr("src", data.resources[0]).fadeIn();
		})
	});
});