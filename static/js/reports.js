$(document).ready(function(){
    $(".fixed-action-btn").floatingActionButton();
    $('.tooltipped').tooltip();
    $('.carousel').carousel({
        numVisible: 5
    });
    $("select").formSelect();
    $("#report_type_selection").parent().parent().hide();
    $("#report_type").change(function(){
        if($(this).prop('checked'))
        {
            $("#report_input_title").text("Adicionar parte de Relatório");
            $("#report_type_selection").parent().parent().show();
        }
        else
        {
            $("#report_input_title").text("Adicionar Relatório Completo");
            $("#report_type_selection").parent().parent().hide();
        }
    });
    $("#save_btn").on("click",function(){
        let formData = {
            "report_input": $("#report_input").val(),
            "report_type_selection": null
        };
        let report_type_selection = $("#report_type_selection");
        if($("#report_type").prop("checked") && report_type_selection.val() !== "")
            formData["report_type_selection"]=report_type_selection.val();
        $.ajax({
            url:"/reports",
            method: "POST",
            data: formData,
            success: data=>{
                data = JSON.parse(data);
                if(data["result"])
                {
                    window.location.reload();
                }
            },
            error: err=>{
                console.error(err);
            }
        });
    });
    $(".carousel-item").click(function () {
        let report_content_text;
        let report_part_content_text;
        let report_input = $("#report_input");
        let report_part_content_type;
        try {
            report_content_text = $(this).find(".report_content").text();
        }catch (exception) {
            report_part_content_text = "";
        }
        try {
           report_part_content_text = $(this).find(".report_part_content").text();
           report_part_content_type = $(this).find(".report_part_content_type").text();
        }catch (exception) {
            report_part_content_text = "";
        }
        if(report_part_content_text !== "")
        {
            let current_text = report_input.text();
            console.log(report_part_content_type);
            switch (report_part_content_type)
            {
                case "header":
                    current_text = report_part_content_text+=current_text;
                    break;
                case "body":
                    break;
                case "footer":
                    current_text+=report_part_content_text;
                    break;
            }
            report_input.text(current_text);
        }
        if(report_content_text !== "")
        {
            report_input.text(report_content_text);
        }
        M.textareaAutoResize(report_input);
        report_input.siblings("label").addClass("active");
    });
});