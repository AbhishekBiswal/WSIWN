$(document).ready(function(){

	$(".magic").click(function(a){
		a.preventDefault();
		var genreone = $("select.first option:selected").attr("data-text");
		var genretwo = $("select.second option:selected").attr("data-text");
		//alert($(".firstgenre").val());
		//alert(genreone);
		$(".wait").show();
		$(".submit").submit();
	});

	$("select.first").change(function(){
		var value = $("select.first option:selected").attr("data-text");
		$(".firstgenre").val(value);
	});

	$("select.second").change(function(){
		var value = $("select.second option:selected").attr("data-text");
		$(".secondgenre").val(value);
	});

}); // ready