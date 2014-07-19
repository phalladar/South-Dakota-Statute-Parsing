#! C:\python27
import re, urllib, pickle
theFakeURL = """


<!DOCTYPE html>

<html>
<head><title>

</title><meta http-equiv="X-UA-Compatible" content="IE=10" /><meta name="viewport" content="width=device-width, initial-scale=1" /><link type="text/css" rel="Stylesheet" href="/inc/styles/styles.css" /><link type="text/css" rel="Stylesheet" href="/inc/styles/print.css" media="print" />
<script type="text/javascript">


    if (/(android|bb\d+|meego).+mobile|webOS|iPhone|iPod|IEMobile|BlackBerry/i.test(navigator.userAgent)) {

        document.write('<link type="text/css" rel="stylesheet" href="/inc/styles/mobile.css" />');
    }
    else {
        document.write('<link href="/inc/styles/screen.css" rel="stylesheet" type="text/css" />');
    }
    
</script>
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<!--[if lt IE 9]>
    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
<!--[if IE 7]>
    <style type="text/css">
        #sitesearch{
            padding-bottom: 10px;
        }
        .searchbutton {
            width: 6%;
            margin-left: -15px;
            padding-right: 10px;
            }
        #committeeevents {
            padding-top: 20px;
    
        }
    </style>
<![endif]-->
<!--[if IE 8]>
    <style type="text/css">
        #sitesearch{
            padding-bottom: 10px;
        }
        .searchbutton {
            margin-left: -2px;
        }
    </style>
<![endif]-->
<script src="/inc/scripts/modernizr.js"></script>

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script>    window.jQuery || document.write('<script src="js/libs/jquery-1.7.min.js">\x3C/script>')</script>

<script defer src="/inc/scripts/jquery.flexslider.js"></script>
<script type="text/javascript">
    $(function () {
    try{
        SyntaxHighlighter.all();}
        catch(e){}
    });
    $(window).load(function () {
        if ($('.flexslider').flexslider) {
            $('.flexslider').flexslider({
                animation: "slide",
                start: function (slider) {
                    $('body').removeClass('loading');
                }
            });
        }
    });
</script>

<script>
    (function (i, s, o, g, r, a, m) {
        i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date(); a = s.createElement(o),
  m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
    })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

    ga('create', 'UA-42867922-1', 'sd.gov');
    ga('send', 'pageview');

</script>
<script language="JAVASCRIPT">
<!--
    if (top.frames.length != 0)
        top.location = self.document.location;
// -->
</script>

<script src="/inc/scripts/crumbs.js"></script>

<meta http-equiv="Pragma" content="no-cache" /><meta http-equiv="Expires" content="-1" /><meta http-equiv="Cache-Control" content="no-cache,no-Store" />
<SCRIPT language="JAVASCRIPT">
<!--
    if (top.frames.length != 0)
        top.location = self.document.location;
// -->
</SCRIPT>

<link rel="icon" type="image/png" href="../../favicon.png" /><link rel="apple-touch-icon" href="/img/icon.png" /><link rel="apple-touch-icon-precomposed" href="/img/icon_composed.png" />
    <script src="/inc/scripts/jquery.js"></script>
<script type="text/javascript">
    $(function () {
        $(window).scroll(function () {
            if ($(this).scrollTop() != 0) {
                $('#toTop').fadeIn();
            } else {
                $('#toTop').fadeOut();
            }
        });

        $('#toTop').click(function () {
            $('body,html').animate({ scrollTop: 0 }, 800);
        });
    });
</script>

    <!--[if lt IE 7]>
        <script defer type="text/javascript" src="scripts/pngfix.js"></script>
    <![endif]-->
    <script type="text/javascript" src="/My_LRC/scripts/mylrc_main.js"></script>
    <script type="text/javascript" src="/My_LRC/scripts/gridview_multiselect.js"></script>

     

    </head>
<body>
    <form method="post" action="DisplayStatute.aspx?Type=Statute&amp;Statute=34A-3A-6" id="form1">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUJNTkwNDk2MzMzD2QWAmYPZBYCAgMPZBYCAggPZBYCAgUPZBYEAgEPZBYEAgMPFgIeCWlubmVyaHRtbAXAGjxkaXYgc3R5bGU9InRleHQtYWxpZ246cmlnaHQiPjxhIGhyZWY9Ii9TdGF0dXRlcy9QcmludGVyU3RhdHV0ZS5hc3B4P1R5cGU9U3RhdHV0ZSZTdGF0dXRlPTM0QS0zQS02IiB0YXJnZXQ9Il9uZXciPlByaW50ZXIgRnJpZW5kbHk8L2E+PC9kaXY+ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCjxIVE1MPg0KPEhFQUQ+DQo8SFRNTD4NCjxIRUFEPg0KPHRpdGxlPjM0QS0zQS02IEV4ZW1wdGlvbiBvZiBwdWJsaWMgd2F0ZXIgc3VwcGx5IHN5c3RlbXMtLVJlcXVpcmVtZW50cy4gPC90aXRsZT4NCjxNRVRBIE5BTUU9IktleXdvcmRzIiBDb250ZW50PSJTb3V0aCBEYWtvdGEgQ29kaWZpZWQgTGF3cyBTRENMIDM0QS0zQS02IEV4ZW1wdGlvbiBvZiBwdWJsaWMgd2F0ZXIgc3VwcGx5IHN5c3RlbXMtLVJlcXVpcmVtZW50cy4gIj4NCjxNRVRBIE5BTUU9IkRlc2NyaXB0aW9uIiBDb250ZW50PSJTb3V0aCBEYWtvdGEgQ29kaWZpZWQgTGF3cyAzNEEtM0EtNiI+DQo8L0hFQUQ+DQo8Qk9EWT4NCg0KPCEtLSBGaWxlIGNvbnZlcnRlZCBieSBXcDJIdG1sIFZlcnNpb24gNC4wICAtLT4NCjwhLS0gRW1haWwgQW5kcmV3QGJyYWNrZW5iZWRzLmNvLnVrIGZvciBtb3JlIGRldGFpbHMgIC0tPg0KDQo8IS0tIFdQIFN0eWxlIE9wZW46IFN5c3RlbV8zNCAtLT48IS0tIFdQIFN0eWxlIEVuZDogU3lzdGVtXzM0IC0tPg0KPERpdiBhbGlnbj0iZnVsbCI+DQo8IS0tIFdQIFBhaXJlZCBTdHlsZSBPbjogU0VOVSAtLT4mbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDs8IS0tIFdQIFN0eWxlIEVuZDogU0VOVSAtLT4NCjM0QS0zQS02Lg0KPCEtLSBXUCBQYWlyZWQgU3R5bGUgT2ZmOiBTRU5VIC0tPiZuYnNwOzwhLS0gV1AgU3R5bGUgRW5kOiBTRU5VIC0tPg0KDQo8IS0tIFdQIFBhaXJlZCBTdHlsZSBPbjogQ0wgLS0+PCEtLSBXUCBTdHlsZSBFbmQ6IENMIC0tPg0KRXhlbXB0aW9uIG9mIHB1YmxpYyB3YXRlciBzdXBwbHkgc3lzdGVtcy0tUmVxdWlyZW1lbnRzLg0KPCEtLSBXUCBQYWlyZWQgU3R5bGUgT2ZmOiBDTCAtLT4gPCEtLSBXUCBTdHlsZSBFbmQ6IENMIC0tPg0KVGhlIHNlY3JldGFyeSBtYXkNCmV4ZW1wdCBhbnkgcHVibGljIHdhdGVyIHN1cHBseSBzeXN0ZW0gZnJvbSBhbnkgbWF4aW11bSBjb250YW1pbmFudCBsZXZlbCB1cG9uIGZpbmRpbmcgdGhhdDo8YnI+DQoNCjwhLS0gV1AgU3R5bGUgT3BlbjogUDEgLS0+PC9EaXY+PERpdiBhbGlnbj0iZnVsbCI+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PCEtLSBXUCBTdHlsZSBFbmQ6IFAxIC0tPg0KKDEpDQo8IS0tIFdQIFN0eWxlIE9wZW46IElOIC0tPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwhLS0gV1AgU3R5bGUgRW5kOiBJTiAtLT4NCkR1ZSB0byBjb21wZWxsaW5nIGZhY3RvcnMsIGluY2x1ZGluZyBlY29ub21pYywgdGhlIHB1YmxpYyB3YXRlciBzeXN0ZW0gaXMgdW5hYmxlIHRvDQpjb21wbHkgd2l0aCB0aGUgY29udGFtaW5hbnQgbGV2ZWwuIEluIGFzc2Vzc2luZyB0aGUgY29tcGVsbGluZyBmYWN0b3JzIHRoZSBzZWNyZXRhcnkgc2hhbGwNCmNvbnNpZGVyIHN1Y2ggZmFjdG9ycyBhcyBjb25zdHJ1Y3Rpb24sIGluc3RhbGxhdGlvbiwgb3IgbW9kaWZpY2F0aW9uIG9mIHRyZWF0bWVudCBlcXVpcG1lbnQNCm9yIHN5c3RlbXMsIGFuZCB0aGUgdGltZSBuZWVkZWQgdG8gcmVwbGFjZSBhbiBleGlzdGluZyBub25jb21wbHlpbmcgZmFjaWxpdHkgd2l0aCBhIG5ldw0KdHJlYXRtZW50IHN5c3RlbTs8YnI+DQoNCjwhLS0gV1AgU3R5bGUgT3BlbjogUDEgLS0+PC9EaXY+PERpdiBhbGlnbj0iZnVsbCI+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PCEtLSBXUCBTdHlsZSBFbmQ6IFAxIC0tPg0KKDIpDQo8IS0tIFdQIFN0eWxlIE9wZW46IElOIC0tPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwhLS0gV1AgU3R5bGUgRW5kOiBJTiAtLT4NClRoZSBwdWJsaWMgd2F0ZXIgc3lzdGVtIHdhcyBpbiBvcGVyYXRpb24gb24gdGhlIGVmZmVjdGl2ZSBkYXRlIG9mIHRoZSBtYXhpbXVtDQpjb250YW1pbmFudCBsZXZlbCByZWd1bGF0aW9uczs8YnI+DQoNCjwhLS0gV1AgU3R5bGUgT3BlbjogUDEgLS0+PC9EaXY+PERpdiBhbGlnbj0iZnVsbCI+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PCEtLSBXUCBTdHlsZSBFbmQ6IFAxIC0tPg0KKDMpDQo8IS0tIFdQIFN0eWxlIE9wZW46IElOIC0tPiZuYnNwOyZuYnNwOyZuYnNwOyZuYnNwOzwhLS0gV1AgU3R5bGUgRW5kOiBJTiAtLT4NClRoZSBncmFudGluZyBvZiB0aGUgZXhlbXB0aW9uIHdpbGwgbm90IHJlc3VsdCBpbiBhbiB1bnJlYXNvbmFibGUgcmlzayB0byBoZWFsdGg7IGFuZDxicj4NCg0KPCEtLSBXUCBTdHlsZSBPcGVuOiBQMSAtLT48L0Rpdj48RGl2IGFsaWduPSJmdWxsIj4mbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDsmbmJzcDs8IS0tIFdQIFN0eWxlIEVuZDogUDEgLS0+DQooNCkNCjwhLS0gV1AgU3R5bGUgT3BlbjogSU4gLS0+Jm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A7PCEtLSBXUCBTdHlsZSBFbmQ6IElOIC0tPg0KV2l0aGluIG9uZSB5ZWFyIG9mIHRoZSBkYXRlIG9mIGV4ZW1wdGlvbiBhdXRob3JpemF0aW9uLCBhIHNjaGVkdWxlIGZvciBjb21wbGlhbmNlIGJlDQppc3N1ZWQgYW5kIHRoZSBvd25lciBvZiB0aGUgc3VwcGx5IGFncmVlIHRvIGltcGxlbWVudCB0aGUgc2NoZWR1bGUuPGJyPg0KPGJyPg0KDQo8IS0tIFdQIFBhaXJlZCBTdHlsZSBPbjogU0NMIC0tPjwhLS0gV1AgU3R5bGUgRW5kOiBTQ0wgLS0+DQo8Yj4gU291cmNlOjwvYj4gIFNMIDE5ODMsIGNoIDI2MCwgJiMxNjc7Jm5ic3A7Ni4NCjwhLS0gV1AgUGFpcmVkIFN0eWxlIE9mZjogU0NMIC0tPjwhLS0gV1AgU3R5bGUgRW5kOiBTQ0wgLS0+DQo8cD4NCjwvQk9EWT4NCjwvSFRNTD4NCjxoci8+ZAIFDxYEHwAFDkNoYXB0ZXIgMzRBLTNBHgRocmVmBS9EaXNwbGF5U3RhdHV0ZS5hc3B4P1N0YXR1dGU9MzRBLTNBJlR5cGU9U3RhdHV0ZWQCAw9kFgICBw8QZGQWAWZkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYCBRNjdGwwMCRidG5TaXRlU2VhcmNoBRNjdGwwMCRidG5CaWxsU2VhcmNosQ/rOcGeXQ7HNMMdGFiLHr8VhZpsFN6CTxJ5QdUhHKA=" />

<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="/wEWBQLhoLfiCALX9KPQCALD4rOHCAL0lOjpBAKI5o+1B2hW8HSogygEmXHimR9cGwTBj+G8t7v8vSbGNTKroPqb" />
        
    <header>
    <a href="/"><img id="sdseal" src="/img/sd-seal.gif" alt="South Dakota Seal" /></a>
    <div id="logotext">
    <a class="homelink" href="/">
    <span id="sdleg">South Dakota Legislature<br /></span>
    <span id="lrctext">Legislative Research Council<br /></span>
    <span id="director">Sue Cichos, Interim Director</span> 
</a>
    </div>


 <div id="sitesearch">
 <div id="pnlSiteSearch">
    
     Site Search:&nbsp;
     <input name="ctl00$sitesearchbox" type="text" id="sitesearchbox" placeholder="Site Search" class="sitesearchbox" />&nbsp;
     <input type="image" name="ctl00$btnSiteSearch" id="btnSiteSearch" class="searchbutton" src="../../img/searchbutton.png" align="top" />
         
</div>
</div>

    <div id="billsearch">
    <div id="pnlBillSearch">
    
     Bill Quickfind:&nbsp;<input name="ctl00$billsearchbox" type="text" id="billsearchbox" placeholder="Bill Number" />&nbsp;
     <input type="image" name="ctl00$btnBillSearch" id="btnBillSearch" class="searchbutton" src="../../img/searchbutton.png" align="top" />
    
</div>
    <br />
    <br /><br />
</div>
    
    </header>
    
    <nav id="navTop" class="mobilenoshow">
        <ul class="dropdown"><li><a href="/Legislative_Session/Menu.aspx"><div>Legislative<br/>Session</div></a><ul><li><a href="/Legislative_Session/Default.aspx?Session=Eighty-Ninth"><div>2014</div></a></li><li><a href="/Legislative_Session/Default.aspx?Session=Eighty-Eighth"><div>2013</div></a></li><li><a href="/Legislative_Session/Default.aspx?Session=Eighty-seventh"><div>2012</div></a></li><li><a href="/Legislative_Session/Default.aspx?Session=Eighty-sixth Special"><div>2011 Special Session</div></a></li><li><a href="/Legislative_Session/Default.aspx?Session=Eighty-sixth"><div>2011</div></a></li><li><a href="/Legislative_Session/Past_Sessions/Default.aspx"><div>Previous Years</div></a></li></ul></li><li class="oneline"><a href="/interim/Menu.aspx"><div>Interim</div></a><ul><li><a href="/interim/Interim.aspx?Session=Eighty-Ninth"><div>2014</div></a></li><li><a href="/interim/Interim.aspx?Session=Eighty-Eighth"><div>2013</div></a></li><li><a href="/interim/Interim.aspx?Session=Eighty-seventh"><div>2012</div></a></li><li><a href="/interim/Interim.aspx?Session=Eighty-sixth"><div>2011</div></a></li><li><a href="/interim/Interim.aspx?Session=Eighty-fifth"><div>2010</div></a></li><li><a href="/interim/default.aspx"><div>Previous Years</div></a></li></ul></li><li class="oneline"><a href="/Statutes/default.aspx"><div>Laws</div></a><ul><li><a href="/Statutes/Constitution/default.aspx"><div>Constitution</div></a></li><li><a href="/Statutes/Codified_Laws/default.aspx"><div>Codified Laws</div></a></li><li><a href="../Session_Laws/menu.aspx"><div>Session Laws</div></a></li></ul></li><li><a href="/Rules/default.aspx"><div>Administrative<br/>Rules</div></a><ul><li><a href="/Rules/RulesList.aspx"><div>Rules List</div></a></li><li><a href="/Rules/TextSearch.aspx"><div>Rules Text Search</div></a></li><li><a href="/Rules/default.aspx"><div>Quick Find</div></a></li><li><a href="/docs/Rules/Register/07142014.pdf"><div>Current Register</div></a></li><li><a href="/Rules/RegisterArchive.aspx"><div>Register Archive</div></a></li><li><a href="/Rules/TextSearch.aspx?Catalog=Register"><div>Register Text Search</div></a></li><li><a href="/Rules/RulesManual.aspx"><div>Rules Manual</div></a></li><li><a href="/Rules/PriceList.aspx"><div>Price List</div></a></li><li><a href="http://rules.sd.gov"><div>Rules SD GOV</div></a></li></ul></li><li class="oneline"><a href="/Legislators/default.aspx?CurrentSession=True"><div>Legislators</div></a><ul><li><a href="/Legislators/Who_Are_My_Legislators/default.aspx?CurrentSession=True"><div>Who Are My Legislators?</div></a></li><li><a href="/Legislators/Legislators/MembersByDistrict.aspx?CurrentSession=True"><div>Listing By District</div></a></li><li><a href="/Legislators/Legislators/default.aspx?CurrentSession=True"><div>Legislators</div></a></li><li><a href="/Legislators/Legislators/Roster.aspx?Body=H&CurrentSession=True"><div>House Roster</div></a></li><li><a href="/Legislators/Legislators/Roster.aspx?Body=S&CurrentSession=True"><div>Senate Roster</div></a></li><li><a href="../../Legislators/Historical_Listing/default.aspx?CurrentSession=True"><div>Historical Listing</div></a></li><li><a href="/docs/legislators/TermLimits.pdf"><div>Legislator Term Limits</div></a></li><li><a href="/docs/legislators/members.xls"><div>Downloadable Address List</div></a></li></ul></li><li class="oneline"><a href="/Budget/Budget_Hearing_Schedule_and_Materials/default.aspx"><div>Budget</div></a><ul><li><a href="/Budget/Current_Interim/default.aspx"><div>Current Interim</div></a></li><li><a href="/Budget/Budget_Hearing_Schedule_and_Materials/default.aspx"><div>Hearing Schedule and Materials</div></a></li><li><a href="/Budget/Reference_Documents/default.aspx"><div>Budget Documents</div></a></li></ul></li><li><a href="/My_LRC/default.aspx"><div>E-Subscribe<br/>(My LRC)</div></a></li><li><a href="/Students_Page/default.aspx"><div>Students' <br/> Page</div></a><ul><li><a href="../../Students_Page/Page/default.aspx"><div>Legislative Page Program</div></a></li><li><a href="../../Students_Page/Intern/Default.aspx"><div>Legislative Intern Program</div></a></li><li><a href="../../Students_Page/Guide/"><div>Students' Guide</div></a></li><li><a href="../../docs/studentspage/idealaw.pdf"><div>How an Idea Becomes Law</div></a></li><li><a href="../../docs/studentspage/HowOld.pdf"><div>How Old do I have to be...</div></a></li><li><a href="../../docs/studentspage/CapitolVisit.pdf"><div>Capitol Visit During Session</div></a></li><li><a href="../../docs/studentspage/FunFacts.pdf"><div>Fun Facts and Trivia</div></a></li><li><a href="../../docs/studentspage/puzzle.pdf"><div>Test Your Knowledge</div></a></li></ul></li><li id="refmat"><a href="/Reference_Materials/default.aspx"><div>Reference<br/>Materials</div></a><ul><li><a href="/docs/referencematerials/legislatorreferencebook.pdf"><div>Legislator Reference Book</div></a></li><li><a href="/Reference_Materials/Issue_Memos/"><div>Issue Memos / White Papers</div></a></li><li><a href="../../docs/referencematerials/draftingmanual.pdf"><div>Legislative Drafting Manual</div></a></li><li><a href="/docs/rules/rulesmanual.pdf"><div>Rules Drafting Manual</div></a></li><li><a href="/Reference_Materials/stats.aspx"><div>Statistical Comparison</div></a></li><li><a href="/docs/general/PersonnelPolicy.pdf"><div>Personnel Policy</div></a></li><li><a href="/Reference_Materials/default.aspx"><div>Link to Other Resources</div></a></li></ul></li></ul></nav>
        
        <div class="crumbformat">
            <script type='text/javascript'>
            <!--
            
                breadcrumbs()
            //-->
            </script>
            
            </div>
        <div id="content">
            <div style="display: inline-block; padding:0; margin:0; width:100%">
                
    <div id="leftcolumn">
        <div id="ContentPlaceHolder1_BlueBoxLeft" class="bluebox">
        <ul><li><a href="/statutes/Codified_Laws/"><div>Title List</div></a></li><li><a href="/statutes/Codified_Laws/TextSearch.aspx"><div>Text Search</div></a></li><li><a href="/statutes/Codified_Laws/QuickFind.aspx"><div>Statute Quick Find</div></a></li></ul></div>
        
    </div>
    <section id="textcolumn">

        <div id="ContentPlaceHolder1_divTop" class="topContent">
        </div>

        <div id="ContentPlaceHolder1_divBottom" class="bottomContent">
            <div id="ContentPlaceHolder1_pnlStatutes" class="Results">
    
                <span id="ContentPlaceHolder1_lblMessage"></span>&nbsp;
                <div id="ContentPlaceHolder1_divStatutes"><div style="text-align:right"><a href="/Statutes/PrinterStatute.aspx?Type=Statute&Statute=34A-3A-6" target="_new">Printer Friendly</a></div>                                                                   
                                                                          
                                                                          
                                                                          
                                                                          
<HTML>
<HEAD>
<HTML>
<HEAD>
<title>34A-3A-6 Exemption of public water supply systems--Requirements. </title>
<META NAME="Keywords" Content="South Dakota Codified Laws SDCL 34A-3A-6 Exemption of public water supply systems--Requirements. ">
<META NAME="Description" Content="South Dakota Codified Laws 34A-3A-6">
</HEAD>
<BODY>
<!-- File converted by Wp2Html Version 4.0  -->
<!-- Email Andrew@brackenbeds.co.uk for more details  -->

<!-- WP Style Open: System_34 --><!-- WP Style End: System_34 -->
<Div align="full">
<!-- WP Paired Style On: SENU -->&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: SENU -->
34A-3A-6.
<!-- WP Paired Style Off: SENU -->&nbsp;<!-- WP Style End: SENU -->

<!-- WP Paired Style On: CL --><!-- WP Style End: CL -->
Exemption of public water supply systems--Requirements.
<!-- WP Paired Style Off: CL --> <!-- WP Style End: CL -->
The secretary may
exempt any public water supply system from any maximum contaminant level upon finding that:<br>

<!-- WP Style Open: P1 --></Div><Div align="full">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: P1 -->
(1)
<!-- WP Style Open: IN -->&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: IN -->
Due to compelling factors, including economic, the public water system is unable to
comply with the contaminant level. In assessing the compelling factors the secretary shall
consider such factors as construction, installation, or modification of treatment equipment
or systems, and the time needed to replace an existing noncomplying facility with a new
treatment system;<br>

<!-- WP Style Open: P1 --></Div><Div align="full">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: P1 -->
(2)
<!-- WP Style Open: IN -->&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: IN -->
The public water system was in operation on the effective date of the maximum
contaminant level regulations;<br>

<!-- WP Style Open: P1 --></Div><Div align="full">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: P1 -->
(3)
<!-- WP Style Open: IN -->&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: IN -->
The granting of the exemption will not result in an unreasonable risk to health; and<br>

<!-- WP Style Open: P1 --></Div><Div align="full">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: P1 -->
(4)
<!-- WP Style Open: IN -->&nbsp;&nbsp;&nbsp;&nbsp;<!-- WP Style End: IN -->
Within one year of the date of exemption authorization, a schedule for compliance be
issued and the owner of the supply agree to implement the schedule.<br>
<br>

<!-- WP Paired Style On: SCL --><!-- WP Style End: SCL -->
<b> Source:</b>  SL 1983, ch 260, &#167;&nbsp;6.
<!-- WP Paired Style Off: SCL --><!-- WP Style End: SCL -->
</BODY>
</HTML>
<hr/></div>
                <a href="DisplayStatute.aspx?Statute=34A-3A&Type=Statute" id="ContentPlaceHolder1_ahrefUpOneLevel">Chapter 34A-3A</a>
            
</div>
            
            <p></p>
        </div>
    </section>

            </div>
    <div id="toTop">^ Back to Top</div>
            
        </div>
        
    <footer>
    <div id="contactinfo">
    
    Capitol Building, 3rd Floor - 500 East Capitol Avenue - Pierre, SD 57501 - 605.773.3251<br /><br />

    <a href="/">Home</a> | <a href="/contact/">Contact</a> | <a href="/contact/help.aspx">Help</a> | <a target="_blank" href="http://sd.gov/privacy.aspx">Privacy Policy</a> | <a target="_blank" href="http://sd.gov">SD Homepage</a><br />
    Copyright &copy; 2013 South Dakota Legislature
    

    
    </div>
    
    </footer>
</form>
</body>
</html>
"""

def read_statute(theURL, theSection):
	#theText = theFakeURL #comment this out and uncomment below line when ready to go live
	theText = urllib.urlopen(theURL).read()
	theBodyText = re.findall(ur'<BODY>(.*)<\/BODY>', theText, re.DOTALL)
	theText = re.sub("&nbsp;", " ", theBodyText[0])
	theText = re.sub(r'(\d*[A-Z]?-\d*[A-Z]?-\d[\.\d]*)', r"\1 ", theText, re.DOTALL)
	theText = re.sub('<!-- WP Style Open: IN -->    <!-- WP Style End: IN -->', " ", theText) # account for indents
	theText = re.sub(r'\<!--.*-->', "", theText)
	theText = re.sub(r'<Div.*\">', "", theText) # clear the div
	theText = re.sub(r'\n|<b>|</b>|\r', " ", theText) # remove the newlines
	theText = re.sub(r'<BR>|<br>', r'\n', theText)
	theText = re.sub("<p>", r'\n', theText)
	theText = re.sub(r" +", " ", theText) # Turn all multiple spaces into a single space
	return theText

theWebStatute = {}
theWebStatute['35-4-2.10'] = read_statute('http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=35-4-2.10', '35-4-2.10')
theWebStatute['34A-3A-6'] = read_statute('http://legis.sd.gov/Statutes/Codified_Laws/DisplayStatute.aspx?Type=Statute&Statute=34A-3A-6', '34A-3A-6')
pickle.dump( theWebStatute, open("webstatutes.p", "wb"))