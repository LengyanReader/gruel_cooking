
const nav=document.getElementById('nav');
window.addEventListener('scroll',()=>{nav.classList.toggle('scrolled',window.scrollY>60)});
const toggle=document.getElementById('langToggle');
const buttons=toggle.querySelectorAll('button');
function setLang(lang){document.body.className='lang-'+lang;buttons.forEach(b=>b.classList.toggle('active',b.dataset.lang===lang));localStorage.setItem('__STORAGE__',lang);document.documentElement.lang=(lang==='zh')?'zh':'en';}
const saved=localStorage.getItem('__STORAGE__');
if(saved)setLang(saved);
buttons.forEach(b=>b.addEventListener('click',()=>setLang(b.dataset.lang)));
