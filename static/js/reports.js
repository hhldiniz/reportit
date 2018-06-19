$(document).ready(function(){
   $(".fixed-action-btn").floatingActionButton();
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
});