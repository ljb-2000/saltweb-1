<%@ page language="java" pageEncoding="utf-8" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<title>新手红包-落地页</title>
<%@ include file="../common/header.jsp" %>
<style>
.guide-box{
	width:100%;  
	background: #b31011 url(../static/images/redenvelopes/down-bg.png) no-repeat center ;
	min-height:2100px; 
}  
.w1020_box {
  width: 1000px;
  height: 2031px;
  position: relative;
  background: url(../static/images/redenvelopes/down_top2.png) no-repeat center;
  margin: auto;  
  }
  
  
/** 他们领取了红包列表 **/
.get_redlist{
	background:url(../static/images/redenvelopes/down_03.png) no-repeat;
	width: 224px; 
	height: 270px; 
	position: absolute; 
	top: 520px;
    left: 706px;
	overflow:hidden; 
	margin-top:20px;
}

.get_redlist ul{
	width: 194px; 
	margin: 53px 15px 0px 15px;
	font-size:16px;
	height:205px;
	overflow:hidden;
}

.get_redlist ul li{
	height:34px;
	line-height:34px;
	border-bottom: 1px dashed #a5a5a5; 
	list-style:none;
}

.get_redlist .border-none{
	border:none; 
}

.yellowdashed_border{
	height:6px;
	background:url(../static/images/redenvelopes/down_06.png) no-repeat;
}

.newbie_downbtn{  
	width: 370px;
	height: 70px;
	background: url(../static/images/redenvelopes/down_btn.png) no-repeat;
	display: block; 
	position: absolute; 
	bottom: 0;
	left: 325px;
}


/**立即领取红包 列表下面的**/
.getact_red1{
	background:url(../static/images/redenvelopes/act_btn_03.jpg) no-repeat;
	width: 195px; 
	height: 48px; 
	position: absolute; 
	top: 288px;
    left: 264px;
}
.getact_red2{
	background:url(../static/images/redenvelopes/act_btn_07.jpg) no-repeat;
	width: 195px; 
	height: 48px; 
	position: absolute; 
	top: 990px;
    left: 104px;
}
/**  注册领红包 **/
.regi_getred{
	width:312px;
	height:auto;
	border:8px solid #fff8a5;
	position:absolute;
	left: 680px;
	top: 60px;
	background-color:#ffd672;
}

.regi_getred table tr{
	height:40px;
	line-height:40px;
}

.regi_getred table{
	font-size:16px;
	color:#7d3600;
	margin:25px 16px auto 16px;;
}
.regi_getred table td input{ 
	border-radius:4px;
	width:100%;
	height:30px;
	line-height:20px;
}

.regi_getred table td input::-webkit-input-placeholder{ 
	color:#bb9d87;
	font-size:14px;
}

.regi_getred table td input::-ms-input-placeholder{ 
	color:#bb9d87;
	font-size:14px;
}

.regi_getred table td input::-moz-placeholder{ 
	color:#bb9d87;
	font-size:14px;
} 

.red-downgetmess{ 
	background-color: #fb110f;
	font-size: 14px;
	display: block;
	color: #ffffff;
	border-radius: 4px;
	height: 30px;
	line-height: 30px;
	margin-top: -9px;
	margin-left: 2px;
    border:none;
}

.red-downgetmess:hover{
	color: #ffffff; 
	background-color:#f13434;
	border:none;
}
/**获取短信验证码 按钮被点击过后的样式**/
.red-downgetmess-clicked {
	background-color: #f4f4f4;
	color: #bb9d87;
	width: 169px;
	margin-left: 2px;
	padding: 0 4px;
	border-radius: 4px;
}

.red-downyzm{
	width: 88px;
	height: 27px;
	display: block;
	margin-top: -8px;
	line-height:21px;
}

.red-downref{
	cursor:pointer;
	margin-top: -10px;
	display: block;
}

/**底部注册领红包大按钮**/
.red-downgetMon{
	width: 100%;
	background-color: #fb110f;
	font-size: 24px;
	display: block;
	color: #ffffff;
	border-radius: 6px;
	height: 55px;
	line-height: 55px;
	text-align: center;
	text-decoration: none;
	border:none;
	margin: 15px 0 25px 0;
}

.red-downgetMon:hover{
	text-decoration: none;
	color: #ffffff; 
	background-color:#f13434;
}
/**错误提示**/
.down-tips{ 
	background-color: #ffdddd;
	border: 1px solid #ffbbbb;  
	font-size:13px;  
	color: #fb110f;
}
.down_span{
	width: 87px;
	display: inline-block;
	margin-left: 0;
}

</style>
 
</head>
<body>
<!--top start-->
<%@ include file="../common/top.jsp" %>
<!-- top over-->

<input id="checkPhoneExp" value="<%=Configuration.getInstance().getValue("check_phone_exp") %>" type="hidden"/>

<!-- main content start-->
<div class="guide-box">   
	<div class="w1020_box"> 
		<div class="regi_getred">
		<form action="${path }/user/iregister.html" method="post" id="regInfo">
			<input type="hidden" id="regFrom" name="regFrom" value="redenvelops" />
			<table>
				<tbody>
				<tr>
					<td width="83px">手机号码</td>
					<td colspan="3" class="pl10"><input type="text" maxlength="11" onkeyup="this.value=this.value.replace(/[^0-9]/g,'')" id="phone" name="phone" placeholder="请输入手机号码"></td>
				</tr>
                <tr>
                    <td width="83px">图片验证码</td>
                    <td class="pl10"><input type="text" style="width:61px;" id="imageCode" name="imageCode"></td>
                    <td class="pl5">
                        <img alt="暂无" id="randImage" src="${path}/randCode/getVerifyCode.html" onclick="loadimage();" style="cursor: pointer;" border="0" class="red-downyzm">
                    </td>
                    <td class="pl5">
                        <h5 onclick="loadimage();" class="blue glyphicon glyphicon-refresh red-downref"></h5>
                    </td>
                </tr>
                <tr>
                    <td width="83px">短信验证码</td>
                    <td colspan="3" class="pl10"><input type="text" id="phoneCode" name="phoneCode" maxlength="4" placeholder="请输入短信验证码"></td>
                </tr>
				<tr>
					<td width="83px"></td>
					<td colspan="3" class="pl10">
						<button type="button" class="red-downgetmess" id="randCode" onclick="sendMobileCode(this);">获取短信验证码</button>
						<!-- 点击发送验证码之后，隐藏按钮 显示如下倒计时信息 start -->
							<!-- <p class='red-downgetmess-clicked' id='sendMsg'>[60]秒后可重新获取</p> -->
						<!-- 点击发送验证码之后，隐藏按钮 显示如下倒计时信息 end -->
					</td> 
				</tr>
				<tr style="height:25px;line-height:25px;" id="errorMsgTr">
					<td colspan="4" class="pl10" id="errorMsg" align="center"></td>
				</tr>
				<tr>
					<td colspan="4">
						<button type="button" class="red-downgetMon" onclick="doSubmit();" >注册领取红包</button>
					</td>
				</tr>
			</tbody>
			</table>
			</form>
		</div>
		<!-- 已领红包列表 -->
		<div class="get_redlist ">
		 <ul id="donwul">
			 <c:forEach items="${list }" var="list">
				<li>
					<span class="down_span" >${list[1] }</span>
					<span class="marginl18" > 领取了红包</span>
				</li>
			</c:forEach>
		  </ul>
    </div> 
	<a href="#" onclick="getPackte()" class="newbie_downbtn" ></a> 
	</div>
</div>

<!-- footer start-->
<%@ include file="../common/myxxd_footer.jsp" %>
<!-- footer over-->

</body>

<script type="text/javascript" src="${path}/static/js/personal/perfectinfo.js"></script>
<script type="text/javascript">

$(function() { 
    var scrollare = $("#donwul"); //定义滚动区域 
    var _interval = 2000; //定义滚动间隙时间 
    var _moving; //需要清除的动画 
    scrollare.hover(function() { 
        clearInterval(_moving); //当鼠标在滚动区域中时,停止滚动 
    },
    function() { 
        _moving = setInterval(function() { 
            var _field = scrollare.find('li:first'); //此变量不可放置于函数起始处,li:first取值是变化的 
            var _h = _field.height(); //取得每次滚动高度 
            _field.animate({  marginTop: -_h + 'px' }, 600,
            function() { //通过取负margin值,隐藏第一行 
                _field.css('marginTop', 0).appendTo(scrollare); //隐藏后,将该行的margin值置零,并插入到最后,实现无缝滚动 
            })
        },
        _interval) //滚动间隔时间取决于_interval 
    }).trigger('mouseleave'); //函数载入时,模拟执行mouseleave,即自动滚动 
}); 


function getPackte(){
	var getPackte = '${getPackte }';
	if(getPackte=='1'){
		$('#atitle_mini').html("抱歉");
		$('#acontent_mini').html("您已经注册过，不能再领取红包喽！");
		$('#alertdiv_mini').modal('show');
		return;
	}else{
		window.location.href="${path}/user/iregister.html";
	}
}


//倒计时时间
var time = 60;
var interval;

/**
 * 填充倒计时
 */
function initdaojishihtml(obj, time) {
	$(obj).html("<p class='red-downgetmess-clicked' id='sendMsg'>[" + time + "]秒后可重新获取</p>");
}

/**
* 短信验证码倒计时
*/
function daojishi(obj,objHtml) {
    time = time - 1;
    if (time < 0) {
        $(obj).html(objHtml);
        //清除定时器
        clearInterval(interval);
    } else {
    	$(obj).html("<p class='red-downgetmess-clicked' id='sendMsg'>[" + time + "]秒后可重新获取</p>");
    }
}

//验证码刷新脚本
function loadRand() {
    clearInterval(interval);
    $("#randSpan").html(m_code);
}

//刷新图片验证码
function loadimage() {
	document.getElementById("randImage").src = "${path}/randCode/getVerifyCode.html?"+ Math.random();
}

var m_code = "<button type='button' class='red-downgetmess' id='randCode' onclick='sendMobileCode(this);' >获取短信验证码</button>";

/**
 * 发送短信验证码
 * @returns
 */
function sendMobileCode(thisObj) {
	var phone = $("#phone").val();
	if(!checkPhone(phone)){
		return;
	}
	time = 60;
    var thisParent = $(thisObj).parent();
    var thisParentHtml = m_code;
    
  	//填充倒计时
    initdaojishihtml(thisParent,time);
   	$.getJSON("${path}/user/sendSMS.html?" + new Date(),
    	{
            phone : phone,
            imageCode : $("#imageCode").val()
        },
        function (data) {
        	if(data.resultCode == 0){
            	interval = setInterval(function(){ daojishi(thisParent,thisParentHtml); }, 1000);
            }else{
            	$("#errorMsgTr").addClass("down-tips");
        		$("#errorMsg").html(data.msg);
                $(thisParent).html(thisParentHtml);
                //清除定时器
                loadRand();
            }
       }
   );
};


/* 发送手机验证码验证 */
function checkPhone(phone){
	var flag = true;
	if(null==phone || ""==phone){
		$("#errorMsgTr").addClass("down-tips");
		$("#errorMsg").html("请输入手机号码！");
		loadimage();
		flag = false;
	}else{
		var exp = $("#checkPhoneExp").val();
        var myreg =  new RegExp(exp);
        if (!myreg.test(phone)) {
        	$("#errorMsgTr").addClass("down-tips");
    		$("#errorMsg").html("请输入有效的手机号码！");
    		loadimage();
    		flag = false;
        }
	}
	$.ajax({
		url:"${path}/user/checkMobile.html",
		type:'POST',
		data:{"mobile":phone},
		async: false,
		success:function(data){	
			if(data == 1){	
				$("#errorMsgTr").addClass("down-tips");						
				$('#errorMsg').html('您输入的手机号已被注册!');	
				loadimage();
				flag = false;
			}
		}
	});	
	if(flag){
		$("#errorMsgTr").removeClass("down-tips");
		$("#errorMsg").html("");
	}
	return flag;
}

/* 校验图片验证码 */
function checkImageCode(imageCode){
	var flag = true;
	$.ajax({
		url:"${path}/user/checkCode.html",
		type:'POST',
		data:{"code":imageCode},
		async: false,
		success:function(data){	
			if(data != 'true'){
				$("#errorMsgTr").addClass("down-tips");
				$("#errorMsg").html("请输入正确的图片验证码！");
				loadimage();
				flag = false;
			}
		}
	});	
	return flag;
}

/* 校验手机验证码 */
function checkPhoneCode(phoneCode){
	var flag = true;
	$.ajax({
		url:"${path}/user/checkSMS.html",
		type:'POST',
		data:{"code":phoneCode},
		async: false,
		success:function(data){	
			if(data != '0'){
				$("#errorMsgTr").addClass("down-tips");
				$("#errorMsg").html("请输入正确的手机验证码！");
				loadimage();
				flag = false;
			}
		}
	});	
	return flag;
}


function doSubmit(){
	var phone = $("#phone").val();
	var phoneCode = $("#phoneCode").val();
	var imageCode = $("#imageCode").val();
	if(null==phone || ""==phone){
		$("#errorMsgTr").addClass("down-tips");
		$("#errorMsg").html("请输入手机号码！");
		loadimage();
		return;
	}else if(null==phoneCode || ""==phoneCode){
		$("#errorMsgTr").addClass("down-tips");
		$("#errorMsg").html("请输入短信验证码！");
		loadimage();
		return;
	}else if(null==imageCode || ""==imageCode){
		$("#errorMsgTr").addClass("down-tips");
		$("#errorMsg").html("请输入图片验证码！");
		loadimage();
		return;
	}
	if(checkPhoneCode(phoneCode) && checkPhone(phone)){
			$("#errorMsgTr").removeClass("down-tips");
			$("#errorMsg").html("");
			$("#regInfo").submit();
	}
}
</script>

</html>