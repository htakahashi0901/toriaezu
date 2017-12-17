//for company num
var companynum;
//cif
var cif;
//company name
var companyname;
//general counter
var i=0;
//tab counter
var j=10;
var k=0;

//alert for counting grid rows
var grid = new Array();
var grid[1-1]=Number(window.prompt("input the number of Direct Shareholders"));
var grid[2-1]=Number(window.prompt("input the number of List the indirect intermediate and ...."));
var grid[3-1]=Number(window.prompt("input the number of Do the following individuals ...."));
var grid[4-1]=Number(window.prompt("Ultimate Parent Companies"));
var grid[5-1]=Number(window.prompt("Do the following Ultimate Parent Company ...."));
var grid[6-1]=Number(window.prompt("items to be confirmed ...."));
var grid[8-2]=Number(window.prompt("Method of .. Counter (Proxy..)"));
var grid[14-7]=Number(window.prompt("Please list the names ..."));
var grid[15-7]=Number(window.prompt("List all products ..."));
var grid[18-9]=Number(window.prompt("Provide all authorised ..."));

// enable dblclick
var event = document.createEvent('MouseEvents');
event.initEvent('dblclick',true,true);

//get the length of the number of all companies
var IGnum=document.getElementsByClassName("gridxCellWidget").length+1;

//tab loop
function tabloop(){
	setTimeout(function(){
		document.getElementsByClassName("tabLabel")[j].click();
		j++;
		if(j<21){
			tabloop();
		}
		},8000);
};

//run excel
var sheet="sheet1";
var filename="C://3340HTakahas//Desktop//cisnet.xlsx";
var filename1="C://3340HTakahas//Desktop//cisnetinput.xlsx";
var excel=new ActiveXObject("Excel.Aplication");
var excel_file=excel.Workbooks.Open(filename);
var excel_file1=excel.Workbooks.Open(filename1);
var excel_sheet;
//load only once the code above
function selectsheet(sheet){
	excel_sheet=excel.Worksheets(sheet);
}

//get start and end row
function getRowNum(start,end,cif,excel_sheet){
		var cellv;
		while(true){
			cellv=excel_sheet.Cells(row,1).Value;
			if(cellv==cif){
				start=row;
				while(true){
					cellv=excel_sheet.Cells(row,1).Value;
					if(cellv!=""){
						end=row;
						break;
					}
					else if(row<10000){
						row++;
					}
					//no end
					else{
						row=0;
						break;
					}
				}
				break;
					
			}
			else if(row<10000){
				row++;
			}
			//no start
			else{
				row=0;
				break;
			}
		}
};

//push the button to add grids
function addGrids(gridindex,num){
	var iter;
	for(iter=0;iter<num;iter++){
		document.getElementsByClassName("dijitReset dijitInline dijitIconaddButton")[gridindex].click();
	}
};

//check string if its date
function dateOrnot(elem){
	var regex=/^[a-zA-Z]{3} [0-9]{2}, [0-9]{4}?$/;
	var regex1=/^[a-zA-Z]{3} [0-9]{1}, [0-9]{4}?$/;
	reruen regex.test(elem) || regex1.test(elem);
};

//input data to grid
function inputData(firstindex,row_n,col_n){
	var count1;
	var index=firstindex;
	for(count1=0;count1<row_n*col_n;count1++){
		//except calendar
		if(dateOrnot(data[count1]) == false){
			//if checkbox
			if(data[count1]=="true" || data[count1]=="false"){
				document.getElementsByClassName("gridxCellWidget")[index].dispatchEvent(event);
				document.getElementsByClassName("dijitReset dijitCheckBoxInput")[4].click();
				index++;				
			}
			else{
				document.getElementsByClassName("gridxCellWidget")[index].dispatchEvent(event);
				dijit.byId(document.getElementsByClassName("gridxCellWidget")[index].Id).setCellValue(data[count1],data[count1],document.getElementsByClassName("gridxCellWidget")[index].Id,true);
				index++;
			}
		}
		//calendar
		else{
			document.getElementsByClassName("gridxCellWidget")[index].dispatchEvent(event);
			document.getElementsByClassName("dijitReset dijitInputInner")[53].value=data[count1];
			dijit.byId(document.getElementsByClassName("dijitReset dijitInputInner")[53].id).openDropDown();
			document.getElementsByClassName("dijitCalendarEnabledDate dijitCalendarCurrentMonth dijitCalendarDateTemplate dijitCalendarSelectedDate")[document.getElementsByClassName("dijitCalendarEnabledDate dijitCalendarCurrentMonth dijitCalendarDateTemplate dijitCalendarSelectedDate").length-1].click();
			index++;
		}
	return index;
	}
};

//load data of grid from excel
function loadexcel(firstindex,grid,cif,cpname){
	var count;
	var count1;
	var count_data;
	var row=1;
	var cellv;
	var start;
	var end;
	var row_n;
	var index=firstindex;
	var data = new Array();
	//need to know the num
	var col_n=[10,10,11,3,4,10,10,10,5,4];
	//process for each grid
	for(count=0;count<grid.length;count++){
		sheet="sheet"+(count+2);
		selectsheet(sheet);
		getRowNum(start,end,cif,excel_sheet);
		row_n=end-start+1;
		count1=start;
		//store values from excel to variables in js
		for(count1=0;count1<row_n*col_n[count];count1++){
			data[count1]=excel_sheet.Cells(start,3+(count1)%(col_n[count]+1)).Value;
		}
		//don't check if some rows already exist.
		addGrids(count,row_n);
		//make the index to input new data
		index=index+grid[count]*col_n[count];
		//input all data for each grid
		index=inputData(index,row_n,col_n);
	}
};

function loadexcel1(cif,cpname){
	var data = new Array();
	var count;
	var count1;
	var row;
	while(true){
		sheet="sheet1";
		selectsheet(sheet);
		if(cif==excel_sheet.Cells(count1,7).Value){
			row = count1;
			break;
		}
		else if(count1<10000){
			count1++;
		}
		else{
			row=0;
			break;
		}
	}
	for(count=0;count<129;count++){
		data[count]=excel_sheet.Cells(row,count).Value;
	}
	for(count=0;count<129;count++){
		document.getElementsByClassName("dijitReset dijitInputInner")[count].value=data[count];
	}
};

function writeexcel(firstindex,grid,cif,cpname){
	var count;
	var row=1;
	var cellv;
	//need to know the num
	var col_n=[10,10,11,3,4,10,10,10,5,4];
	//unless gridlength is 10 need to check
	for(count=0;count<grid.length;count++){
		sheet="sheet"+(count+2);
		selectsheet(sheet);
		while(true){
			cellv=excel_sheet.Cells(row,3).Value;
			if(cellv!="" && row < 10000){
				row++;
			}
			else{
				break;
			}
		}
		excel_sheet.Cells(row,1).Value=cif;
		excel_sheet.Cells(row,2).Value=cpname;
		for(row;row<row+grid[count];row++){
			for(col=3;col<col_n+3;col++){			
				excel_sheet.Cells(row,col).Value=document.getElementsByClassName("gridxCellWidget")[firstindex].innerHTML;
				firstindex++;
			}
		}
	}
};

//main
function mainloop(){
	setTimeout(function(){
//dblclick on a company name
document.getElementsByClassName("gridxCellWidget")[companynum].dispatchEvent(event);
//meaningful donothing for-loop
for(k=0;k<1000000;k++){};
//load all tabs
tabloop();
j=10;
//read cif and company name
cif=document.getElementsByClassName("dijitReset dijitInputInner")[6].value;
companyname=document.getElementsByClassName("dijitReset dijitInputInner")[7].value;
//take backup to excel
writeexcel(IGnum,grid,cif,companyname);
alert("if the excel is messy, the member of grid may not be correct.")
//load values for grid from excel to cisnet
loadexcel(IGnum,grid,cif,companyname);
//load values for except grid
loadexcel1(cif,companyname);
//close this company
companynum++;
//open next company
if(companynum<IGnum){
	mainloop();
}
},10000);
};
