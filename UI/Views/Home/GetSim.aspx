<%@ Page Title="" Language="C#" MasterPageFile="~/Views/Shared/Site.Master" Inherits="System.Web.Mvc.ViewPage<dynamic>" %>

<asp:Content ID="Content1" ContentPlaceHolderID="TitleContent" runat="server">
    GetSim
</asp:Content>

<asp:Content ID="Content2" ContentPlaceHolderID="MainContent" runat="server">


<fieldset>
<legend>Similarity Matrix</legend>  
    <!--h2> Test Web URL </h2--> <h3><%: ViewData["url"] %></h3>
    <div class="CSS_Table_Example" style="width:600px;height:150px;">
			<table>
				<tr> 
					<td>
						Content Similarity Score
					</td>
					<td >
						Visual Similarity Score
					</td>
					<td>
						Link Similarity SCore
					</td>
                    <td>
						Structural Similarity SCore
					</td>
				</tr>
				<tr>
					<td align="center">
						<%: ViewData["contentSimScore"]%>
					</td>
					<td align="center">
						<%: ViewData["visualSimScore"] %>
					</td>
					<td align="center">
						<%: ViewData["linkSimScore"]%>
					</td>
                    <td align="center">
						<%: ViewData["structuralSimScore"]%>
					</td>
				</tr>
				
				</table>
		</div>
       <div id="gauge"></div>
</fieldset>

<input id="totalSim" type="hidden" value = "<%= ViewData["totalSim"] %>" />

        <script>
            $(document).ready(function () {
                createGauge();
            });

            function createGauge(labelPosition) {
                $("#gauge").kendoRadialGauge({

                    pointer: {
                        value: $("#totalSim").val()
                    },

                    scale: {
                        minorUnit: 5,
                        startAngle: -30,
                        endAngle: 210,
                        max: 100,
                        labels: {
                            position: labelPosition || "outside"
                        },
                        ranges: [
                                {
                                    from: 25,
                                    to: 50,
                                    color: "#ffc700"
                                }, {
                                    from: 50,
                                    to: 75,
                                    color: "#ff7a00"
                                }, {
                                    from: 75,
                                    to: 100,
                                    color: "green"
                                }
                            ]
                    }
                });
            }


        </script>
                    <style scoped>
                #gauge-container {
                    background: transparent url("../../Content/images/gauge-container.png") no-repeat 50% 50%;
                    width: 404px;
                    height: 404px;
                    text-align: center;
                    margin: 20px 10px 30px 50px;
                }

                #gauge {
                    width: 330px;
                    height: 330px;
                    margin: 0 auto 0;
                }
            </style>
</asp:Content>
