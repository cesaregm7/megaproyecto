var module1 = 1;
var module2 = 1;
var module3 = 1;
var module4 = 1;

var contenido1=["<div class=''><span class='mod-1-bold'>El Centro Integral de Psicología Aplicada (CIPA)</span>, fue previamente conocido como Centro de Apoyo Integral a la Comunidad (CAIC). Fundado en el año 2002 por iniciativa de la Dra. María Del Pilar Grazioso y el equipo docente de la licenciatura. En el año 2014 luego de un plan de ampliación del centro se le modificó el nombre a CIPA, para brindar servicios en diferentes áreas de la psicología <span class='mod-1-bold'>(Industrial/Organizacional, Neuropsicología, Psicología Comunitaria, Educativa, etc.) y un componente de investigación aplicada en los campos de educación, salud y bienestar integral.</span> Los estudiantes de la Licenciatura en Psicología, Maestría en Consejería Psicológica y Salud Mental, Maestría en Neuropsicología Clínica y Doctorado en Psicología Aplicada pueden realizar sus prácticas profesionales en el Centro.</div>","<div class=''><div class=''>Las prácticas profesionales que se pueden realizar dentro de CIPA son las de <span class='mod-1-bold'>psicoterapia (individual, pareja, familiar y grupal), evaluación neuropsicológica y psicoeducativa, programas de intervención en el aprendizaje,</span> entre otros.</div><div class=''><img src='' /></div><br/><div class=''>El horario de atención es de <span class='mod-1-bold'>lunes a jueves de 8:30 a 17:00, los viernes es de 13:00 a 17:00, y los sábados es de 8:00 a 13:00</span>. El cliente se contacta por medio de vía telefónica, correo electrónico o puede presentarse físicamente.</div></div>","<div class=''><div class=''><div class=''>“Somos un centro de formación e investigación interdisciplinario, para el entrenamiento de profesionales en las ciencias psicológicas en la región hispanoamericana que ofrece servicios a la sociedad fundamentados con principios éticos.”</div><div class=''><img src=''></div></div><div class=''><div class=''><img src=''></div><div class=''>“Ser en la región interamericana en el campo de las ciencias psicológicas el centro de formación, investigación y servicio interdisciplinario de excelencia por su nivel académico y contribución a la sociedad.”</div></div></div>","<div class=''><ul><li>Facilitar un ambiente de entrenamiento que permita adquirir y fomentarlas destrezas fundamentales necesarias para llevar a cabo un proceso de psicoterapia, consejería o evaluación.</li> <li>Desarrollar conciencia, profesional y personal, sobre la importancia de un psicoterapeuta/consejero/evaluador.</li><li>Identificar la identidad profesional por medio del desarrollo de un estilo propio, genuino, ético y competente.</li><li>Adquirir las competencias y ampliar los conocimientos necesarios para trabajar de una forma efectiva y ética con clientes de diferentes poblaciones y culturas.</li><li>Crear conciencia de la importancia de adquirir competencias multiculturales que permitan el ser un profesional ético, empático, tolerante y eficiente.</li><li>Fortalecer las destrezas existentes e integrarlas al desarrollo de nuevas competencias que permitan ejercer la profesión de la mejor manera.</li><li>Crear conciencia sobre la importancia de hacer investigación y brindar el espacio para hacerlo.<li></ul></div>"];

function nextPhotoM1(){
	var gallery1 = document.getElementById('g-mod-1');
	if (module1==7)
		document.getElementById('next1').disabled=true;
	else{
		module1++;
		document.getElementById('prev1').disabled=false;
	}
	if (module1==7){
		document.getElementById('next1').disabled=true;
		document.getElementById('iniciar-evaluacion').style.visibility = "visible";
	}

	gallery1.innerHTML = contenido1[module1];
} 

/*function nextPhotoM1(){
	var gallery1 = document.getElementById('g-mod-1');
	if (module1==7)
		document.getElementById('next1').disabled=true;
	else{
		module1++;
		document.getElementById('prev1').disabled=false;
	}
	if (module1==7){
		document.getElementById('next1').disabled=true;
		document.getElementById('iniciar-evaluacion').style.visibility = "visible";
	}
	gallery1.src="/static/images/modulo1-"+module1+".png";
} */

function prevPhotoM1(){
	var gallery1 = document.getElementById('g-mod-1');
	document.getElementById('iniciar-evaluacion').style.visibility="hidden";
	if (module1==1)
		document.getElementById('prev1').disabled=true;
	else{
		module1--;
		document.getElementById('next1').disabled=false;
	}
	if (module1==1)
		document.getElementById('prev1').disabled=true;

	gallery1.src="/static/images/modulo1-"+module1+".png";
} 

function nextPhotoM2(){
	var gallery2 = document.getElementById('g-mod-2');
	if (module2==9)
		document.getElementById('next2').disabled=true;
	else{
		module2++;
		document.getElementById('prev2').disabled=false;
	}
	if (module2==9){
		document.getElementById('next2').disabled=true;
		document.getElementById('iniciar-evaluacion').style.visibility = "visible";
	}
	gallery2.src="/static/images/modulo2-"+module2+".png";
} 

function prevPhotoM2(){
	var gallery2 = document.getElementById('g-mod-2');
	document.getElementById('iniciar-evaluacion').style.visibility="hidden";
	if (module2==1)
		document.getElementById('prev2').disabled=true;
	else{
		module2--;
		document.getElementById('next2').disabled=false;
	}
	if (module2==1)
		document.getElementById('prev2').disabled=true;

	gallery2.src="/static/images/modulo2-"+module2+".png";
}

function nextPhotoM3(){
	var gallery3 = document.getElementById('g-mod-3');
	if (module3==11)
		document.getElementById('next3').disabled=true;
	else{
		module3++;
		document.getElementById('prev3').disabled=false;
	}
	if (module3==11){
		document.getElementById('next3').disabled=true;
		document.getElementById('iniciar-evaluacion').style.visibility = "visible";
	}
	gallery3.src="/static/images/modulo3-"+module3+".png";
} 

function prevPhotoM3(){
	var gallery3 = document.getElementById('g-mod-3');
	document.getElementById('iniciar-evaluacion').style.visibility="hidden";
	if (module3==1)
		document.getElementById('prev3').disabled=true;
	else{
		module3--;
		document.getElementById('next3').disabled=false;
	}
	if (module3==1)
		document.getElementById('prev3').disabled=true;

	gallery3.src="/static/images/modulo3-"+module3+".png";
} 
