$(function(){
    $('form').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: "http://localhost:61090/ProductService.svc/Library/" + $("#txt").val(),
            type: "GET",
            success: function(data){
                console.log(data.GetBookByIdResult);
                $("#daily").text(data.GetBookByIdResult.Name) 
                //$("#promotional").text(data.GetBookByIdResult.Name) 
                $("#price").text(data.GetBookByIdResult.Price) 
                $("#mass").text(data.GetBookByIdResult.Mass) 
                $("#mass").text(data.GetBookByIdResult.ingradients) 
               
               
               
                $(`<tr><td>${data.GetBookByIdResult.Name}</td><td>${data.GetBookByIdResult.Price}</td><td>${data.GetBookByIdResult.Mass}</td><td>${data.GetBookByIdResult.Ingradients}</td><td>${data.GetBookByIdResult.Image}</td></tr>`).appendTo("#container")
            }

    });
    })
});
