<%@ Page Language="C#" MasterPageFile="~/Views/Shared/Site.Master" Inherits="System.Web.Mvc.ViewPage" %>

<asp:Content ID="Content1" ContentPlaceHolderID="TitleContent" runat="server">
    Home Page
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">
    <h2>insight of your site</h2>
    
    <% using (Html.BeginForm("HandleForm", "Home"))
       {%>
    <fieldset>
        <legend>User Data</legend>
         <div class="editor-label">
           <b>URL of User Website 1</b>
        </div>
        <div class="editor-field">
            <input type="text" class="k-textbox" name="URL1" id="URL1" />
            
        </div>
        <br />
        <div class="editor-label">
          <b> URL of User Website 2 </b>
        </div>
        <div class="editor-field">
            <input type="text" class="k-textbox" name="URL2" id="URL2" />
            
        </div>

        </br>
         <p>
            <input type="submit" value="Submit" class="k-button"/>
        </p>
    
  
    <%} %>

    <% if (ViewData["URL1"]!=null ){%>
    <fieldset>
    <legend>Submitted Data</legend>
        <form method=post action="/Home/GetSim">
        
        
        <div >
        <%: ViewData["URL1"] %>
        </div>
        
        <div >
        <%: ViewData["URL2"] %>
        </div>
            <p>
            <input type="submit" value="Get Similarity" class="k-button" />
        </p>
        

        
        
    
   

   </form>
    <%} %>

     </fieldset>
      </fieldset>
</asp:Content>
