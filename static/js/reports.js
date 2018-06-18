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
   $("#save_btn").click(function(){
      let data = new FormData();
      data.append("report_input", $("#report_input").val());
      let report_type_selection = $("#report_type_selection");
      if($("#report_type").prop("checked") && report_type_selection.val() !== "")
         data.append("#report_type_selection", report_type_selection.val());
      $.ajax({
         url:"/reports",
         method: "POST",
         data: data,
         success: data=>{

         },
         error: err=>{

         }
      });
   });
});