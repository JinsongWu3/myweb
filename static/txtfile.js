function submit_txt(form, url_name) {
    $("#preview").removeAttr("disabled");
    $.ajax({


        //几个参数需要注意一下
        type: "POST",//方法类型
        dataType: "json",//预期服务器返回的数据类型
        url: url_name,//url
        data: $("#" + form).serialize(),
        success: function (result) {
            console.log(result);//打印服务端返回的数据(调试用)
            if (result.resultCode == 200) {
                $("#preview").removeAttr("disabled");
                $("#preview").trigger("click");
            }
        },
        error: function () {
            alert("ERROR！");
        }
    });


}

