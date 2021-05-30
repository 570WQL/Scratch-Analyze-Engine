import json
from tkinter import filedialog
import zipfile
import os
import time
file = filedialog.askopenfilename()
file = zipfile.ZipFile(file, "r")
# 注意这里的sjwj是文字。
sjwj = file.read(file.namelist()[0]).decode()
import io,json,traceback;#m
# [
# [
#   clts,sjwj;
#   jg结果
#   i,j,m,jg;
#   cl处理 cz查找 wz位置 wb文本 sz数组
#   clwbwz,clwbczwb,clwbczsz;
#   sj数据 mz名字 wz位置 sz数值 wb文本 ts提示 wj文件
#   sjmz,sjwz,sjsz,sjwb,sjts,sjwjwz;
#   mz名字 bj标记 wz位置 dq当前 lx类型 js结束 sx顺序
#   js角色 jm积木 dy定义 bl变量 wt舞台(舞台变量) wb文本
#   zx造型 sy声音 bj背景 ts特殊
#   bg表格(对应表)
#   cljswz,cljssz,  cljsmzdq,           cljsjs;
#   cljmbj,cljmwz,cljmwzbg,cljmwzdq,cljmlxdq,cljmjs;
#   cldymz,cldybj,cldywz;
#   clblbj;
#   clwtbj;
#   cljmsxbg,cljmsxdq,cljmsxbj;# 特殊积木顺序
#   clwt,clwbjs;# 是否为舞台，结束位置
#   cltswtjmwz,cltswtjmlx,cltsjsbj,cltsbjbj;
#   cltsjsjmwz,cltsbj;# 特殊检测
#   xs显示 gs个数
#   xswt;
#   xsblmz, xsblgs;
#   xswtmz, xswtgs;
#   xsdymz, xsdywz;
#   xsbg,xsbgwb,xsbgjm,xsbgjs,xsbgfy;
#   xsjg,xsjmwz,xsjmjg;
#   jc检查
#   jcwt,    jcjg;
#   sy使用 kt开头
#   jcblmz,  jcblgs,  jcblsy;
#   jcwtmz,  jcwtgs,  jcwtsy;
#   jcdymz,  jcdywz,  jcdysy;
#   jcjmlxdq,jcjmktdq,jcwjwzdq,jcjswzdq,jcjmlb;
#   jcjm0001,jcjm0002,jcjm0003,jcjm0004;
#   jcjm0101,jcjm0102,jcjm0302,jcjm0314;
#   积木是否一步执行，检查定义当前位置(-1表示没有定义)，定义之间的相互使用，定义是否一步执行，不适合一步执行的积木列表，定义是否被检查过
#   jcjmyb,jcdywzdq,jcdyxhsy,jcdyyb,jcjgyb;
#   jcjm03dy,jcjm03wz,jcjmcsbj,jcjmcssy;

#   xscw;
clwbczwb="";
clts=1;
xscw=[];
#  sjwj=io.open("input.txt").read();
#  fy翻译
cljmsxbg=[
    "#control_if",
    "NK",
    "#control_if_else",
    "NK2",
    "#control_repeat_until",
    "NK",
    "#control_repeat",
    "SK",
    "#control_while",
    "NK",
    "#control_for_each",
    "EK",
    "#control_wait_until",
    "N",
    "#control_all_at_once",
    "K",
    "#operator_or",
    "12",
    "#operator_and",
    "12",
    "#operator_not",
    "D"
];
cltswtjmlx=[
    "motion_goto_menu",
    "motion_glideto_menu",
    "motion_pointtowards_menu",
    "control_create_clone_of_menu",
    "sensing_touchingobjectmenu",
    "sensing_distancetomenu",
    "sensing_of_object_menu"
];
# ] 开始 [
def start():
    global jcjg;
    # ks开始
    sjks();
    clwj("1");
    # sjmz.append("--------");
    sjwz.append(len(sjsz));
    # tssj();
    # yy语言
    xsyy("直观");
    # xswj(sjwjwz[0],i,True);
    jcjg=[];
    jcks();
    jcwj(sjwjwz[0]);
    jcjgxs();
    # tscw();

# ] cl处理 [
# [
def sjks():
    global sjwb,sjmz,sjwz,sjsz,sjts,sjwjwz;
    sjwb=[];
    sjmz=[];
    sjwz=[];
    sjsz=[];
    sjts=[];
    sjwjwz=[];

def sjzj(mz):
    sjmz.append(mz);
    sjwz.append(len(sjsz));
    sjts.append("");

def clwj(wjwz):
    global clwtbj,cltsjsbj,cltswtjmwz,cljswz,cljsjs,j;
    clwtbj=[];
    cltsjsbj=[];
    cltsjsbj.append("_myself_");
    cltsjsbj.append("_mouse_");
    cltsjsbj.append("_random_");
    cltsjsbj.append("_stage_");
    cltsjsbj.append("_edge_");
    cltswtjmwz=[];
    cljswz=[];
    clwbcz('],"monitors":[',0,len(sjwj),False);
    cljsjs=jg;
    j=0;
    clwbcz('{"isStage":',j,cljsjs,True);
    while(i!=-1):
        cljs();
        clwbcz('{"isStage":',i,cljsjs,True);
    sjwjwz.append(len(sjmz));
    sjzj(wjwz);
    j=0;
    while(j<len(cljswz)):
        sjsz.append(cljswz[j]);
        j+=1;
    cltswtjm();

def cljs():
    global cljsmzdq,clwt,i,cljssz,j,cljmjs,cltsjsjmwz;
    if(sjwj[i]=="t"):
        cljsmzdq="(舞台)";
        clwt=1;
    else:
        i+=13;# "name"
        clwbwb();
        cljsmzdq=jg;
        clwbdx(jg);
        cltsjsbj.append(jg);
        clwt=0;
    cljssz=[];
    cljssz.append(len(sjmz));
    clbl();
    j=i;
    clwbcz('},"comments":{',i,cljsjs,False);
    cljmjs=i;
    cltsjsjmwz=[];
    cljm(j,len(sjsz));
    cljssz.append(len(sjmz));
    sjzj("##jm");
    j=0;
    while(j<len(cljmwz)):
        sjsz.append(cljmwz[j]);
        j+=1;
    cljssz.append(len(sjmz));
    sjzj("##dy");
    j=0;
    while(j<len(cldymz)):
        sjsz.append(cldymz[j]);
        sjsz.append(cldywz[j]);
        # print(cldywz)
        j+=1;
    cljswz.append(len(sjmz));
    sjzj(cljsmzdq);
    j=0;
    while(j<3):
        sjsz.append(cljssz[j]);
        j+=1;
    i=cljmjs;
    cltsjsjm();
    # print(clblbj,cljmbj)
    # print(clvarin,cljmckn)

def clbl():
    global clblbj,j;
    clblbj=[];
    sjzj(0);# 变量数目
    clbl1("V",'},"lists":{');
    sjmz[len(sjmz)-1]=len(clblbj);
    clbl1("L",'},"broadcasts":{');
    if(clwt==1):
        j=0;
        while(j<len(clblbj)):
            clwtbj.append(clblbj[j]);
            j+=1;
def clbl1(lx,jswb):
    global j,clwbjs,i;
    j=i;
    clwbcz(jswb,i,cljsjs,False);
    clwbjs=i;
    # print(j,clwbjs);
    clwbcz('":["',j,clwbjs,True);
    while(i!=-1):
        cljmjc();
        # print(clwbwz,i,sjwj.slice(i-20,i+20))
        if(clwbwz>-1):
            i-=1;
            clwbwb();
            sjsz.append(jg);
            clwbdx(jg);
            clblbj.append(lx+jg);
            # print(clblbj)
        clwbcz('":["',i,clwbjs,True);
    i=clwbjs;

# ] cljm处理积木 [
def cljm(kswz,sjkswz):
    global cljmwz,cljmwzbg,cljmbj,cldymz,cldywz,cldybj,i,m,j;
    cljmwz=[];
    cljmwzbg=[];
    cljmwzbg.append(0);
    cljmbj=[];
    cldymz=[];
    cldywz=[];
    cldybj=[];
    i=kswz;
    clwbcz('":',j,cljmjs,True);
    while(i!=-1):
        # print(i,sjwj.slice(i-20,i+250))
        if(sjwj[i]+sjwj[i+1]+sjwj[i+3]+sjwj[i+4]=='[1,"'):# ":12~3,"
            m=sjwj[i+2];
            if(contains("23",m)):
                cljmbl();
        else:
            clwbqm('{"opcode":"',i);
            if(clwbwz==-1):# opcode
                cljm1();
        clwbcz('":',i,cljmjs,True);
        # print("a",i)
    j=sjkswz;
    while(j<len(sjsz)):
        if(sjsz[j]>0 and sjsz[j]<1000000):
            sjsz[j]=cljmwzbg[sjsz[j]];
        j+=1;
    j=0;
    while(j<len(cljmwz)):
        cljmwz[j]=cljmwzbg[cljmwz[j]];
        j+=1;
    # print(cljmjs)
    i=cljmjs;

def cljm1():
    global i,cljmwzdq,cljmlxdq,j,cljmsxdq,clwbjs,m;
    i=jg-20;
    clbhjm();
    cljmwzdq=jg;
    cljmwzbg[cljmwzdq]=len(sjmz);
    i+=12;
    clwbwb();
    cljmlxdq=jg;
    cltsjm();
    sjzj(cljmlxdq);
    i+=9;# "next"
    if(sjwj[i]=="n"):
        sjsz.append(0);
    else:
        i+=1;
        clbhjm();
        sjsz.append(jg);
    # print(cljmsxbg)
    j=indexof(cljmsxbg,"#"+cljmlxdq);
    if(j>-1):
        cljmsxdq=cljmsxbg[j+1];
        # print(cljmsxdq)
        j=0;
        while(j<len(cljmsxdq)):
            sjsz.append(0);
            j+=1;
    else:
        cljmsxdq="";
    # print("1",i,cljmjs,sjwj.slice(i,i+100))
    clwbcz(',"inputs":{',i,cljmjs,False);
    j=i;
    # print(2,i,cljmjs,sjwj.slice(i,i+100))
    clwbcz('},"fields":{',i,cljmjs,False);
    cljmsr(j,i);
    j=i;
    clwbcz('},"shadow":',i,cljmjs,False);
    # print(3,i,cljmjs,sjwj.slice(i,i+100))
    clwbjs=i;
    clwbcz('":[',j,clwbjs,True);
    j=0;
    while(i!=-1):
        m=sjwj[jg-1];
        if(not contains(",:{\\",m)):# 防止误判
            if(sjwj[i]=="n"):
                sjsz.append(0);
            else:
                if(j==0):
                    clwbqm2("data_",cljmlxdq);
                    if(clwbwz==-1):
                        # print(cljmlxdq,require("util").inspect(String,True,null))
                        if(contains(cljmlxdq,"list")):
                            clbhbl("L",2000000);
                        else:
                            clbhbl("V",2000000);
                    else:
                        if(cljmlxdq=="control_for_each"):
                            clbhbl("V",2000000);
                        else:
                            clbhwb(False);
                    j=1;
                else:
                    clbhwb(False);
                sjsz.append(jg);
        clwbcz('":[',i,clwbjs,True);
    clwbcz('e,"topLevel":',clwbjs,cljmjs,False);
    # print(jmckop,i,sjwj.slice(i,i+50))
    if(sjwj[i]=="t"):
        cljmwz.append(cljmwzdq);
    # print(i)
    # i=clwbjs;
    if(cljmlxdq=="procedures_call"):
        clbhdy();
        sjsz.append(jg);
    else:
        if(cljmlxdq=="procedures_prototype"):
            clbhdy();
            cldywz[jg-3000001]=len(sjmz)-2;#  !!!
            # print(cldywz,jg)
            sjsz.append(jg);
            cljmdyyb();
            if(jg==1):
                cldywz[jg-3000001]*=-1;
    # print(i)

def cljmsr(kswz,jswz):
    global i,cljmsxbj,clwbwz,jg,j;
    i=kswz;
    clwbcz('":[',i,jswz,True);
    while(i!=-1):
        cljmsxbj=sjwj[jg-1];
        clwbwz=-1;
        if(clwbwz==-1):#  !!! 防止误判
            if(contains("123",sjwj[i]) and sjwj[i+1]==','):# '":1~3,'
                i+=2;
                if(sjwj[i]=="n"):
                    # print("null",sjwj[i-2],sjwj.slice(i-10,i+10))
                    if(sjwj[i-2]=="3"):
                        # print("dete")
                        jg=99999999;# 错误
                    else:
                        jg=0;
                        sjts[len(sjts)-1]="1缺少积木";
                else:
                    cljmsz();
                # print("cljmwz1",cljmsxdq,cljmsxbj,jg)
                if(cljmsxdq!=""):
                    # print("sj",cljmsxdq,cljmsxbj)
                    j=0;
                    while(j<len(cljmsxdq) and cljmsxdq[j]!=cljmsxbj):
                        j+=1;
                    if(j!=len(cljmsxdq)):
                        sjsz[len(sjsz)-len(cljmsxdq)+j]=jg;
                else:
                    if(jg!=99999999):
                        sjsz.append(jg);
        clwbcz('":[',i,jswz,True);
    if(cljmsxdq!=""):
        j=0;
        while(j<len(cljmsxdq)):
            if(sjsz[len(sjsz)-len(cljmsxdq)+j]==0):
                sjts[len(sjts)-1]="1缺少积木";
            j+=1;
    i=jswz;

def cljmsz():
    global i,m;
    if(sjwj[i]=='"'):
        i+=1;
        clbhjm();
    else:
        if(sjwj[i+1]=="1"):
            m=sjwj[i+2];
            i+=4;
            if(m=="2"):
                clbhbl("V",1000000);
            else:
                if(m=="3"):
                    clbhbl("L",1000000);
                    sjts[len(sjwz)-1]="4直接引用列表";
                else:
                    clbhwb(True);
        else:
            i+=3;
            clbhwb(True);
def cljmbl():
    global i;
    i=jg-20;
    clbhjm();
    cljmwzbg[cljmwzdq]=len(sjmz);
    cljmwz.append(cljmwzdq);
    if(m=="2"):
        i+=6;
        clbhbl("V",1000000);
    else:
        if(m=="3"):
            i+=6;
            clbhbl("L",1000000);
    sjzj("_");
    sjsz.append(0);
    sjsz.append(jg);

def cljmjc():
    global j;
    j=i-5;
    # print(j,sjwj[j])
    while(j>0 and sjwj[j]!='"'):#  !!! sc2
        if(sjwj[j]=='\\'):
            j=-1;
            return;
        j-=1;
    if(j>i-5-20):
        j=-1;
def cljmdyyb():
    global j,clwbjs,jg,i;
    j=i;
    clwbcz('":{"opcode":',i,cljmjs,True);
    if(i==-1):
        clwbjs=cljmjs;
    else:
        clwbjs=i;
    clwbcz(']","warp":"True"}}',j,clwbjs,True);
    # print(i,sjwj.slice(i,i+20))
    if(i>-1):
        jg=1;
    else:
        jg=0;
        i=j;
# ] clts处理特殊 [
def cltsjm():
    if(clts==0):
        return;
    if(cljmlxdq=="looks_backdrops"):
        cltswtjmwz.append(len(sjmz));
    else:
        if(cljmlxdq=="looks_nextbackdrop"):
            cltswtjmwz.append(1000000+len(sjmz));
        else:
            if(includes(cltswtjmlx,cljmlxdq)):
                cltswtjmwz.append(-len(sjmz));
    if(cljmlxdq=="looks_costume"):
        cltsjsjmwz.append(len(sjmz));
    else:
        if(cljmlxdq=="looks_nextcostume"):
            cltsjsjmwz.append(1000000+len(sjmz));
        else:
            if(cljmlxdq=="sound_sounds_menu"):
                cltsjsjmwz.append(-len(sjmz));
def cltswtjm():
    global j,m;
    if(clts==0):
        return;
    j=0;
    # print(cltswtjmwz,cltsbjbj,cltsjsbj)
    while(j<len(cltswtjmwz)):
        m=cltswtjmwz[j];
        if(m<0):
            clwbdx(sjwb[-sjsz[sjwz[-m]+1]-1]);
            if(not includes(cltsjsbj,jg)):
                sjts[-m]="0角色不存在";
        else:
            if(m>=1000000):
                if(len(cltsbjbj)==1):
                    sjts[m-1000000]="0只有一个背景";
            else:
                clwbdx(sjwb[-sjsz[sjwz[m]+1]-1]);
                if(not includes(cltsbjbj,jg)):
                    sjts[m]="0背景不存在";
                else:
                    if(len(cltsbjbj)==1):
                        sjts[m]="3只有一个背景";
        j+=1;
def cltsjsjm():
    global cltsbjbj,j,m;
    if(clts==0):
        return;
    cltsjsjm1('],"sounds":[');
    # print("costume",i,cltsbj)
    if(clwt==1):
        cltsbjbj=[];
        j=0;
        while(j<len(cltsbj)):
            cltsbjbj.append(cltsbj[j]);
            j+=1;
    else:
        j=0;
        while(j<len(cltsjsjmwz)):
            m=cltsjsjmwz[j];
            if(m>0):
                if(m>=1000000):
                    if(len(cltsbj)==1):
                        sjts[m-1000000]="0只有一个造型";
                else:
                    clwbdx(sjwb[-sjsz[sjwz[m]+1]-1]);
                    if(not includes(cltsbj,jg)):
                        sjts[m]="0造型不存在";
                    else:
                        if(len(cltsbj)==1):
                            sjts[m]="3只有一个造型";
            j+=1;
    cltsjsjm1('],"volume":');
    # print("sounds",i,cltsbj)
    j=0;
    while(j<len(cltsjsjmwz)):
        m=cltsjsjmwz[j];
        if(m<0):
            clwbdx(sjwb[-sjsz[sjwz[-m]+1]-1]);
            if(not includes(cltsbj,jg)):
                sjts[-m]="0声音不存在";
        j+=1;
def cltsjsjm1(jswb):
    global cltsbj,j,clwbjs,i;
    cltsbj=[];
    j=i;
    clwbcz(jswb,i,cljsjs,False);
    clwbjs=i;
    # print(j,clwbjs);
    clwbcz(',"name":"',j,clwbjs,True);
    while(i!=-1):
        i-=1;
        clwbwb();
        clwbdx(jg);
        cltsbj.append(jg);
        clwbcz(',"name":"',i,clwbjs,True);
    i=clwbjs;

# ] clbh处理编号 [
def clbhbl(lx,blwz):
    global jg;
    clwbwb();
    clwbdx(jg);
    jg=lx+jg;
    # var xxxx=jg;
    if(includes(clblbj,jg)):
        jg=blwz+indexof(clblbj,jg)+1;
    else:
        if(includes(clwtbj,jg)):
            jg=-blwz-indexof(clwtbj,jg)-1;
        else:
            jg=9999999;
            # print("v",xxxx,jg,clblbj,clwtbj)
            # undefined.x
def clbhdy():
    global i,m,jg;
    clwbcz(',"proccode":"',i,cljmjs,False);
    i-=1;
    clwbwb();
    m=jg;
    clwbdx(jg);
    if(not includes(cldybj,jg)):
        cldybj.append(jg);
        cldymz.append(m);
        cldywz.append(0);
    jg=3000001+indexof(cldybj,jg);

def clbhjm():
    global i,jg;
    i-=1;
    clwbwb();
    clwbdx(jg);
    if(not includes(cljmbj,jg)):
        cljmbj.append(jg);
        cljmwzbg.append(0);
    jg=indexof(cljmbj,jg)+1;

def clbhwb(kgjc):
    global jg;
    clwbwb();
    if(kgjc and jg!="" and (jg[0]==" " or jg[len(jg)-1]==" ")):
        sjts[len(sjwz)-1]="4输入内容左/右端有空格";
    sjwb.append(jg);
    jg=-len(sjwb);

# ] clwb处理文本 [
# cz查找 hlcw忽略错误 dx大写 wb文本 qm前面
def clwbcz(wb,kswz,jswz,hlcw):# jg:文本前位置 i:文本后位置
    global clwbczsz,i,clwbwz,clwbczwb,jg;
    if(wb!=clwbczwb):
        clwbczsz=[];
        i=0;clwbwz=0;
        while(i<len(wb)):
            if(i>clwbwz and wb[i]==wb[clwbwz]):
                clwbwz+=1;
                i+=1;
                clwbczsz.append(clwbwz);
            else:
                if(clwbwz==0):
                    clwbczsz.append(clwbwz);
                    i+=1;
                else:
                    clwbwz=clwbczsz[clwbwz-1];
        clwbczwb=wb;
    i=kswz;
    clwbwz=0;
    while(i<jswz):
        if(clwbwz==len(wb)):
            jg=i-len(wb);
            return;
        else:
            if(sjwj[i]==wb[clwbwz]):
                clwbwz+=1;
                i+=1;
            else:
                if(clwbwz==0):
                    i+=1;
                else:
                    clwbwz=clwbczsz[clwbwz-1];
    if(not hlcw):
        raise("无法找到"+wb);
    i=-1;

def clwbdx(st):
    global jg,clwbwz;
    # $c=x;
    jg="";
    clwbwz=0;
    while(clwbwz<len(st)):
        if(contains("ABCDEFGHIJKLMNOPQRSTUVWXYZ",st[clwbwz])):
            jg=jg+"#";
        jg=jg+st[clwbwz];
        clwbwz+=1;
def clwbwb():
    global jg,i;
    jg="";
    # if(sjwj[i-1]=='"')raise("clwbwb")
    if(sjwj[i]=='"'):
        i+=1;
        while(i<len(sjwj) and sjwj[i]!='"'):
            jg+=sjwj[i];
            if(sjwj[i]=="\\"):
                jg+=sjwj[i+1];
                i+=1;
            i+=1;
    else:
        while(i<len(sjwj) and not contains(",]}",sjwj[i])):
            jg+=sjwj[i];
            i+=1;
def clwbqm(wb,kswz):
    global clwbwz;
    clwbwz=0;
    while(clwbwz<len(wb)):
        if(sjwj[kswz+clwbwz]!=wb[clwbwz]):
            return;
        clwbwz+=1;
    clwbwz=-1;

def clwbqm2(wb,wb2):
    global clwbwz;
    clwbwz=0;
    while(clwbwz<len(wb)):
        if(wb2[clwbwz]!=wb[clwbwz]):
            return;
        clwbwz+=1;
    clwbwz=-1;

# ]
# ] xs显示 [
# [
# yy语言 sj缩进
def xsyy(lang):
    global xsbg,i,xsbgwb,xsbgjm,xsbgjs,xsbgfy;
    xsbg=json.loads(io.open("SAE-TABLE.js").read());
    i=indexof(xsbg,"##"+lang);
    i+=1;
    xsbgwb=[];
    while(i<len(xsbg) and xsbg[i]!=''):
        xsbgwb.append(xsbg[i]);
        i+=1;
    i+=1;
    xsbgjm=[];
    while(i<len(xsbg) and xsbg[i]!=''):
        xsbgjm.append(xsbg[i]);
        i+=1;
    i+=1;
    xsbgjs=[];
    while(i<len(xsbg) and xsbg[i]!=''):
        xsbgjs.append(xsbg[i]);
        i+=1;
    i+=1;
    xsbgfy=[];
    while(i<len(xsbg) and xsbg[i]!=''):
        xsbgfy.append(xsbg[i]);
        i+=1;
    # print(i,xsbgwb,xsbgjm,xsbgfy,xsbgjs)

def xswj(wjwz,ii,xs):
    global xswtmz,i,xswt;
    xswtmz=[];
    if(xs):
        print(sjmz[wjwz]);
    i=sjwz[wjwz];
    xswt=1;
    if(xs):
        while(i<sjwz[wjwz+1]):
            xsjs(sjsz[i],i,True);
            xswt=0;
            i+=1;
    else:
        xsjs(sjsz[i],i,False);
        xswt=0;
    i=ii;

def xsjs(jswz,ii,xs):
    global i;
    if(xs):
        print(" "+sjmz[jswz]);
    i=sjwz[jswz];
    xsbl(sjsz[i+0],i,xs);
    xsdy(sjsz[i+2],i,xs);
    if(xs):
        xsjm(sjsz[i+1],i);
    i=ii;

def xsbl(blwz,ii,xs):
    global xsblgs,xsblmz,i,xswtgs,j;
    xsblgs=sjmz[blwz];
    xsblmz=[];
    if(xs):
        print("  "+"bl");
    i=sjwz[blwz];
    while(i<sjwz[blwz+1]):
        if(xs):
            if(i==sjwz[blwz]+sjmz[blwz]):
                print("  "+"lb");
            print("   "+sjsz[i]);
        xsblmz.append(sjsz[i]);
        i+=1;
    if(xswt==1):
        xswtgs=xsblgs;
        j=0;
        while(j<len(xsblmz)):
            xswtmz.append(xsblmz[j]);
            j+=1;
    i=ii;

def xsdy(blwz,ii,xs):
    global xsdymz,xsdywz,i;
    xsdymz=[];
    xsdywz=[];
    if(xs):
        print("  "+"dy");
    i=sjwz[blwz];
    while(i<sjwz[blwz+1]):
        if(xs):
            print("   "+sjsz[i+1]+":"+sjsz[i]);
        xsdymz.append(sjsz[i]);
        xsdywz.append(sjsz[i+1]);
        i+=2;
    # print(xsdymz,xsdywz)
    i=ii;

# ] xsjm显示积木 [
# ms模式 jmdj积木等级 jmkh积木括号 jmmb积木模板
def xsjm(jmwz,ii):
    global i,xsjg,j;
    print("  "+"jm"+jmwz);
    i=sjwz[jmwz];
    while(i<sjwz[jmwz+1]):
        xsjg=["   "];
        if(i>sjwz[jmwz]):
            print("  "+"--------");
        xsjm0(sjsz[i],"   ",'@',0,i,j);
        j=0;
        while(j<len(xsjg)):
            print(xsjg[j]);
            j+=1;
        i+=1;
    i=ii;

def xsjm0(jmwz,sj,ms,jmdj,ii,jj):
    global j,jg,i;
    # xsjg[len(xsjg)-1]+="{"+jmwz+"}";
    # print("xsjm0",xsjmwz,jmwz)
    # if(jmwz==1)undefined.x
    if(Math.abs(jmwz)<=1000000):
        if(jmwz>0):
            # print(627,jmwz)
            xsjm1(jmwz,sj,jmdj);
        else:
            if(jmwz==0):
                xsjg[len(xsjg)-1]+=xsbgwb[4];# empty
            else:
                j=1;
                jg=sjwb[-jmwz-1];
                # @纯引用$角色引用&翻译引用%序号引用
                if(ms=='$'):
                    i=indexof(xsbgjs,"#"+jg);
                    if(i>-1):
                        jg=xsbgjs[i+1];
                if(ms=='&'):
                    i=indexof(xsbgfy,"#"+jg);
                    if(i>-1):
                        jg=xsbgfy[i+1];
                if(ms[0]=='%'):
                    i=indexof(xsbgfy,ms);
                    if(i>-1):
                        jg=xsbgjs[i+Number(jg)];
                if(ms=="@"
                 and  (xsbgwb[11]!="Yes"
                  or isNaN(Number(jg))
                  or jg=="")):
                    jg=xsbgwb[0]+jg+xsbgwb[1];
                xsjg[len(xsjg)-1]+=jg;
    else:
        if(Math.abs(jmwz)<=2000000):
            # print(xsblmz,xsblgs)
            xsjmbl(jmwz,1000000);
        else:
            if(Math.abs(jmwz)==9999999):
                jg="？？？";
            else:
                xsjmbl(jmwz,2000000);
        xsjg[len(xsjg)-1]+=jg;
    i=ii;
    j=jj;

def xsjmbl(jmwz,blwz):
    global i,jg;
    if(jmwz>=0):
        i=jmwz-blwz-1;
        jg=xsblmz[i];
        # print("xsjmbl",jmwz,i,jg,xsblgs)
        if(i>=xsblgs):
            i=7;
        else:
            i=5;
    else:
        i=-jmwz-blwz-1;
        jg=xswtmz[i];
        # print("xsjmbl",jmwz,i,jg,xswtgs)
        if(i>=xswtgs):
            i=7;
        else:
            i=5;
    # if(jg==undefined):
        # print(jmwz,i,xswtmz,xsblmz)
        # undefined.x
    # }
    jg=xsbgwb[i]+jg+xsbgwb[i+1];

def xsjm1(jmwz,sj,jmdj):
    global xsjmjg,m,i,jg,j;
    if(xsjmwz==jmwz):
        xsjmjg=len(xsjg)-1;
    # if(xxx>50)undefined.x
    # xxx++
    m=sjmz[jmwz];
    if(m=="procedures_call" or m=="procedures_prototype"):
        i=sjwz[jmwz+1];
        # print(xsdymz,i,sjsz.slice(sjwz[jmwz],i),sjsz[i-1])
        jg=xsdymz[sjsz[i-1]-3000001];
        xsjmdy(jmwz,sj,jg);
    else:
        i=indexof(xsbgjm,"#"+m);
        if(i==-1):
            xsjm3(jmwz,sj,m);
        else:
            j=0;
            if(i+2<len(xsbgjm) and String(xsbgjm[i+2])[0]!="#"):
                j=xsbgjm[i+2];
            # print("xsjmdj",j,jmdj)
            xsjmdj(j,jmdj);
            xsjm2(jmwz,sj,xsbgjm[i+1],j,jg);
    i=sjsz[sjwz[jmwz]];
    if(i!=0):
        xsjg.append(sj);
        # print("sjwz[i]",jmwz,m,sjwz[jmwz],i)
        # if(i<0 or i>1000000):
            # print("err!",i,jmwz,sjmz[jmwz],sjsz.slice(sjwz[jmwz],sjwz[jmwz+1]))
        # }
        # if(jmwz==undefined):
            # undefined.x
        # }
        xsjm1(i,sj,jmdj);#  !!! optimize
def xsjm2(jmwz,sj,jmmb,jmdj,jmkh):
    global i,j,m;
    if(jmkh==1):
        xsjg[len(xsjg)-1]+=xsbgwb[2];
    i=sjwz[jmwz];
    j=0;
    # print("jmmb",jmmb)
    while(j<len(jmmb)):
        # @纯引用$角色引用&翻译引用%序号引用^无括引用#块引用
        m=jmmb[j];
        if(m=='^'):
            if(i+Number(jmmb[j+1])>=sjwz[jmwz+1]):
                xsjg[len(xsjg)-1]+="{Error}";
            else:
                xsjm0(sjsz[i+Number(jmmb[j+1])],sj,'@',0,i,j);
            j+=1;
        else:
            if(m=='#'):
                if(i+Number(jmmb[j+1])>=sjwz[jmwz+1]):
                    xsjg[len(xsjg)-1]+="{Error}";
                else:
                    xsjg.append(sj+xsbgwb[9]);
                    # print("call",sjsz[i+Number(jmmb[j+1])],jmmb[j+1])
                    xsjm0(sjsz[i+Number(jmmb[j+1])],sj+xsbgwb[9],'@',jmdj,i,j);
                j+=1;
                if(j+1<len(jmmb)):
                    xsjg.append(sj);
                else:
                    xsjg.append(sj+xsbgwb[10]);
            else:
                if(contains('@$&%',m)):
                    if(i+Number(jmmb[j+1])>=sjwz[jmwz+1]):
                        xsjg[len(xsjg)-1]+="{Error}";
                    else:
                        if(m=='%'):
                            m+=sjmz[jmwz];
                        if(jmmb[j+1]=="1"):
                            # print(jmmb,j,i,"jmwz",jmwz,sjsz[i+1])
                            xsjm0(sjsz[i+1],sj,m,-Math.abs(jmdj),i,j);
                        else:
                            xsjm0(sjsz[i+Number(jmmb[j+1])],sj,m,jmdj,i,j);
                    j+=1;
                else:
                    if(m=='`'):
                        j+=1;
                    xsjg[len(xsjg)-1]+=jmmb[j];
        j+=1;
    if(jmkh==1):
        xsjg[len(xsjg)-1]+=xsbgwb[3];
def xsjm3(jmwz,sj,lx):
    global i;
    if(not (includes(xscw,lx))):
        xscw.append(lx);
    xsjg[len(xsjg)-1]+="{"+lx;
    # print("i",i,sjwz[i],sjwz[i+1])
    i=sjwz[jmwz]+1;
    while(i<sjwz[jmwz+1]):
        # print("i",i,sjsz[j])
        xsjg[len(xsjg)-1]+=" ";
        xsjm0(sjsz[i],sj,'@',0,i,j);
        i+=1;
    xsjg[len(xsjg)-1]+="}";

def xsjmdy(jmwz,sj,jmmb):
    global i,j;
    # print("jmmb",jmmb,sjsz.slice(sjwz[jmwz],sjwz[jmwz+1]))
    i=sjwz[jmwz]+1;
    j=0;
    while(j<len(jmmb)):
        if(jmmb[j]=='%'):
            if(i>=sjwz[jmwz+1]-1):
                xsjg[len(xsjg)-1]+="{Error}";
            else:
                xsjm0(sjsz[i],sj,'@',0,i,j);
            i+=1;
            j+=1;
        else:
            xsjg[len(xsjg)-1]+=jmmb[j];
        j+=1;
def xsjmdj(x,y):
    global jg;
    jg=0;
    if(x!=0 and Math.abs(x)<Math.abs(y)):
        jg=1;
    if(Math.abs(x)==Math.abs(y) and y>0):
        jg=1;
# ]
# ] ts调试 [
def tssj():
    global i,j;
    i=0;
    while(i<len(sjmz)):
        print(i,sjmz[i]);
        j=sjwz[i];
        while(j<sjwz[i+1]):
            print("  "+sjsz[j]);
            j+=1;
        i+=1;
    # print(sjmz,sjwz,sjsz,clwbjs,cljmwz,cldymz,sjwb);

def tscw():
    global i,j;
    i=0;
    while(i<len(xscw)):
        j=indexof(xsbgjm,"#"+xscw[i]);
        print("    "+JSON.stringify("#"+xscw[i])+",");
        if(j==-1):
            print("    "+JSON.stringify("!!!")+",");
        else:
            j+=1;
            while(j<len(xsbgwb) and xsbgjm[j][0]!="#"):
                print("    "+JSON.stringify(xsbgjm[j])+",");
                j+=1;
        i+=1;
# ] jc检查 [
# [
# zj增加 sr输入 ks开始 js结束
def jcwj(wjwz):
    global jcwjwzdq,jcwtmz,jcwtsy,i,jcwt;
    jcwjwzdq=wjwz;
    jcwtmz=[];
    jcwtsy=[];
    i=sjwz[wjwz];
    jcwt=1;
    while(i<sjwz[wjwz+1]):
        jcjs(sjsz[i],i);
        jcwt=0;
        i+=1;
    i=0;
    while(i<len(jcwtmz)):
        if(jcwtsy[i]==0):
            jcjgzj2("9有变量未被使用",jcwtmz[i]);
        i+=1;
def jcjs(jswz,ii):
    global jcjswzdq,i;
    jcjswzdq=jswz;
    i=sjwz[jswz];
    jcbl(sjsz[i+0],i);
    jcdy(sjsz[i+2],i);
    jcjm(sjsz[i+1],i);
    if(jcwt==0):
        i=0;
        while(i<len(jcblmz)):
            if(jcblsy[i]==0):
                jcjgzj2("9有变量未被使用",jcblmz[i]);
            i+=1;
    i=0;
    while(i<len(jcdymz)):
        if(jcdysy[i]==0):
            # print(jcdywz[i]);
            jcjgzj1(jcdywz[i],jcdywz[i],"9定义积木没有被使用");
        i+=1;
    i=ii;

def jcbl(blwz,ii):
    global jcblgs,jcblmz,jcblsy,i,jcwtgs,j;
    jcblgs=sjmz[blwz];
    jcblmz=[];
    jcblsy=[];
    i=sjwz[blwz];
    while(i<sjwz[blwz+1]):
        jcblmz.append(sjsz[i]);
        jcblsy.append(0);
        i+=1;
    if(jcwt==1):
        jcwtgs=jcblgs;
        j=0;
        while(j<len(jcblmz)):
            jcwtmz.append(jcblmz[j]);
            jcwtsy.append(jcblsy[j]);
            j+=1;
    i=ii;

def jcdy(blwz,ii):
    global jcdymz,jcdywz,jcdysy,jcdyxhsy,jcdyyb,i;
    jcdymz=[];
    jcdywz=[];
    jcdysy=[];
    jcdyxhsy=[];
    jcdyyb=[];
    i=sjwz[blwz];
    while(i<sjwz[blwz+1]):
        jcdymz.append(sjsz[i]);
        jcdywz.append(sjsz[i+1]);
        jcdysy.append(0);
        jcdyyb.append(0);#m
        i+=2;
    i=ii;

# ] jcjm检查积木 [
def jcjm(jmwz,ii):
    global jcjgyb,i,jcjmktdq,jcjmyb,jcjmlb,jg;
    # print("  "+"jm"+jmwz);
    jcjgyb=[];
    i=sjwz[jmwz];
    while(i<sjwz[jmwz+1]):
        jcjmktdq=sjsz[i];
        jcjmyb=0;
        jcjmlb=[];
        try:#m
            jcjmktks(jcjmktdq,i);#m
        except BaseException as err:#m
            traceback.print_tb(err.__traceback__);#m
            print(String(err));#m
            jcjgzj(jmwz,"9SAE 内部错误: "+String(err));#m
        jcjm0(jcjmktdq,i,j);
        try:#m
            jcjmktjs(jcjmktdq,i);#m
        except BaseException as err:#m
            traceback.print_tb(err.__traceback__);#m
            print(String(err));#m
            jcjgzj(jmwz,"9SAE 内部错误: "+String(err));#m
        i+=1;
    jg=1;
    while(jg==1):
        i=0;
        jg=0;
        while(i<len(jcdyxhsy)):
            # print(jcdyyb,jcdyxhsy,i)#m
            if(jcdyyb[jcdyxhsy[i+0]]==1
             and jcdyyb[jcdyxhsy[i+1]]!=1):
                jcdyyb[jcdyxhsy[i+1]]=1;
                jg=1;
            i+=2;
    i=0;
    while(i<len(jcjgyb)):
        # print(i,jcjgyb,jcjgyb[i+1],jcdyyb)#m
        if(jcdyyb[jcjgyb[i+1]]==1):
            jcjgzj1(jcjgyb[i+2],jcjgyb[i+0],jcjgyb[i+3]);
            jcjgzj1(jcdywz[jcjgyb[i+1]],jcjgyb[i+0],":可能会被一步执行的积木");
        i+=4;
    i=ii;

def jcjm0(jmwz,ii,jj):
    global jcjmlxdq,i,j;
    if(jmwz>0 and jmwz<=1000000):
        # print("jcjm0[i]",sjmz[jmwz],jmwz)
        jcjmlxdq=sjmz[jmwz];
        try:#m
            jcjmdg(jmwz,sjwz[jmwz],sjwz[jmwz+1]);#m
        except BaseException as err:#m
            traceback.print_tb(err.__traceback__);#m
            print(String(err));#m
            jcjgzj(jmwz,"9SAE 内部错误: "+String(err));#m
        if(jcjmlxdq=="procedures_call" or jcjmlxdq=="procedures_prototype"):
            i=sjwz[jmwz+1];
            jcjmdy(jmwz);
        else:
            jcjm1(jmwz);
        i=sjsz[sjwz[jmwz]];
        if(i!=0):
            # print("sjwz[i]",sjwz[jmwz],i)
            jcjm0(i,i,j);#  !!! optimize
    else:
        if(jmwz>1000000 and jmwz<=2000000):
            jcblsy[jmwz-1000001]=1;
        else:
            if(jmwz<-1000000 and jmwz>=-2000000):
                jcwtsy[-jmwz-1000001]=1;
    i=ii;
    j=jj;

def jcjmbl(jmwz):
    # print(jcjmlxdq,jmwz)
    if(jmwz>0):
        jcblsy[jmwz-2000001]=1;
    else:
        jcwtsy[-jmwz-2000001]=1;
def jcjm1(jmwz):
    global jcjmyb,i;
    # print("i",i,sjwz[i],sjwz[i+1])
    if(sjmz[jmwz]=="control_all_at_once"):
        jcjmyb+=1;
    jcjmlb.append(jmwz);
    i=sjwz[jmwz]+1;
    while(i<sjwz[jmwz+1]):
        # print("i",i,sjsz[i])
        jcjmlb.append(i-sjwz[jmwz]);
        jcjm0(sjsz[i],i,j);
        jcjmlb.pop();
        i+=1;
    if(sjmz[jmwz]=="control_all_at_once"):
        jcjmyb-=1;
    jcjmlb.pop();

def jcjmdy(jmwz):
    global i;
    # print(jmmb)
    i=sjsz[sjwz[jmwz+1]-1]-3000001;
    i=sjwz[jmwz]+1;
    while(i<sjwz[jmwz+1]-1):
        if(sjsz[i]==0):
            jcjgzj(jmwz,"1缺少积木");
        jcjm0(sjsz[i],i,j);
        i+=1;
# ] jcjg检查结果 [
def jcjgzj(jmwz,wb):
    jcjgzj1(jmwz,jcjmktdq,wb);

def jcjgzj1(jmwz,jmkt,wb):
    jcjg.append(jcwjwzdq);
    jcjg.append(jcjswzdq);
    jcjg.append(jmkt);
    jcjg.append(jmwz);
    jcjg.append(wb);

def jcjgzjyb(jmwz,wb):
    global jg,i;
    if(jcjmyb!=0):
        jg=jcjmktdq;
        i=2;
        while(i<len(jcjmlb)):
            if(sjmz[jcjmlb[i]]=="control_all_at_once"):
                jg=jmwz;
            i+=2;
        jcjgzj(jmwz,wb);
        jcjgzj(jg,":一步执行的积木");
    else:
        if(jcdywzdq!=-1):#m
            jcjgyb.append(jcjmktdq);
            jcjgyb.append(jcdywzdq);#m
            jcjgyb.append(jmwz);
            jcjgyb.append(wb);
def jcjgzj2(wb,sm):
    jcjg.append(jcwjwzdq);
    jcjg.append(jcjswzdq);
    jcjg.append("");
    jcjg.append(sm);
    jcjg.append(wb);

def jcjgxs():
    global i,xsjmwz,xsjmjg,xsjg,j,m;
    i=0;
    while(i<len(jcjg)):
        print("文件 "+sjmz[jcjg[i+0]]);
        print("角色 "+sjmz[jcjg[i+1]]);
        if(jcjg[i+2]==""):
            print(jcjg[i+4]+":"+jcjg[i+3]);
        else:
            # print("  积木 "+sjmz[jcjg[i+2]]);
            # print("  积木 "+sjmz[jcjg[i+3]]);
            print(jcjg[i+4]);
            print("");
            xswj(jcjg[i+0],i,False);
            xsjs(jcjg[i+1],i,False);
            xsjmwz=jcjg[i+3];
            xsjmjg=-1;
            xsjg=[];
            xsjg.append("");
            xsjm0(jcjg[i+2],"",'@',0,i,j);
            if(xsjmjg==-1):
                print("(无法查看预览)");
            else:
                j=xsjmjg-5;
                if(j>len(xsjg)-11):
                    j=len(xsjg)-11;
                if(j<0):
                    j=0;
                m=0;
                while(m<11 and j+m<len(xsjg)):
                    if(j+m==xsjmjg):
                        print("["+String(j+m)+"]	"+xsjg[j+m]);
                    else:
                        print(" "+String(j+m)+"	"+xsjg[j+m]);
                    m+=1;
        i+=5;
        print("");
        print("");
# ]
# ]
# ] 自定义规则 [
# [
# 检查一组积木开始时调用
def jcjmktks(jmwz,ii):
    global jcjmcsbj,jcjmcssy,i,j,m,jcjmyb,jcdywzdq;
    jcjmcsbj=[];
    jcjmcssy=[];
    if(jmwz>0 and jmwz<=1000000):
        if(sjmz[jmwz]=="procedures_definition"):
            if(not includes(jcdywz,jmwz)):
                # print(jcdywz,jmwz)
                jcjgzj(jmwz,"0重复的积木定义");
            i=sjsz[sjwz[jmwz]+1];
            if(i>0 and i<=1000000):
                j=sjwz[i]+1;
                while(j<sjwz[i+1]-1):#m
                    # print(j,i,sjwz[i],sjwz[i+1],sjsz[j])#m
                    m=sjmz[sjsz[j]];#m
                    if(m=="argument_reporter_string_number"):
                        m=sjsz[sjwz[sjsz[j]]+1];
                        clwbdx(sjwb[-m-1]);
                        # print(jmwz,j,jg,jcjmcsbj)
                        jcjmcsbj.append("S"+jg);
                        jcjmcssy.append(0);
                    if(m=="argument_reporter_boolean"):
                        m=sjsz[sjwz[sjsz[j]]+1];
                        clwbdx(sjwb[-m-1]);
                        # print(jmwz,j,jg,jcjmcsbj)
                        jcjmcsbj.append("B"+jg);
                        jcjmcssy.append(0);
                    j+=1;
                i=sjsz[sjwz[i+1]-1];
                if(i>3000000):
                    i-=3000001;#m
                    if(jcdywz[i]<0):
                        jcjmyb+=1;
                    jcdywzdq=i;
        else:
            jcdywzdq=-1;
            if(not contains(sjmz[jmwz],"_when")
             and sjmz[jmwz]!="control_start_as_clone"
             or sjsz[sjwz[jmwz]]==0):
                jcjgzj(jmwz,"0未拼合的积木");
    i=ii;

# 检查一组积木结束时调用
def jcjmktjs(jmwz,ii):
    global i,j,m;
    if(jcdywzdq!=-1):
        i=0;
        j=sjsz[sjwz[jmwz]+1];
        j=sjwz[j]+1;
        # print(jcjmcsbj)
        while(i<len(jcjmcssy)):
            if(jcjmcssy[i]==1):
                m=sjsz[sjwz[sjsz[j]]+1];
                jcjgzj(jcjmktdq,"3有自定义参数没被使用:"+sjwb[-m-1]);
            i+=1;
            j+=1;
    i=ii;

# 检查单个积木时调用srks输入开始srjs输入结束
def jcjmdg(jmwz,srks,srjs):
    jcjm00(jmwz,srks,srjs);
    jcjm01(jmwz,srks,srjs);
    jcjm02(jmwz,srks,srjs);
    jcjm03(jmwz,srks,srjs);
    jcjm04(jmwz,srks,srjs);

# 参数 定义 等待 判断
def jcjm00(jmwz,srks,srjs):
    global m,i;
    # print(jcjmlxdq)
    if(sjts[jmwz]!=""):
        jcjgzj(jmwz,sjts[jmwz]);
    if(jcjmlxdq=="argument_reporter_string_number"):
        m=sjsz[srks+1];
        clwbdx(sjwb[-m-1]);
        i=indexof(jcjmcsbj,"S"+jg);
        if(i==-1):
            jcjgzj(jmwz,"3意外的参数");
        else:
            jcjmcssy[i]+=1;
    if(jcjmlxdq=="argument_reporter_boolean"):
        m=sjsz[srks+1];
        clwbdx(sjwb[-m-1]);
        i=indexof(jcjmcsbj,"B"+jg);
        if(i==-1):
            jcjgzj(jmwz,"3意外的参数");
        else:
            jcjmcssy[i]+=1;
    i=indexof(jcjm0001,jcjmlxdq);
    if(i>-1):
        if(i<5):
            jcjmbl(sjsz[srjs-1]);
        else:
            jcjmbl(sjsz[srjs-2]);
    if(jcjmlxdq=="procedures_call"):
        i=sjsz[sjwz[jmwz+1]-1]-3000001;
        # print("jcdysy",i,jcdysy,jcdymz[i])
        jcdysy[i]=1;
        if(jcdywz[i]==0):
            jcjgzj(jmwz,"0找不到积木定义");
        else:
            if(jcjmyb!=0):
                jcdyyb[i]=1;
            if(jcdywzdq!=-1):
                jcdyxhsy.append(jcdywzdq);
                jcdyxhsy.append(i);
    if(contains(jcjmlxdq.lower(),"wait")
     or includes(jcjm0004,jcjmlxdq)):
        jcjgzjyb(jmwz,"2在一步执行中使用等待积木");
        return;
    if(not includes(jcjm0003,sjmz[jmwz])):
        i=srks+1;
        while(i<srjs):
            m=sjsz[i];
            if(m>0 and m<=1000000):
                if(includes(jcjm0002,sjmz[m])):
                    jcjgzj(m,"2可能放错位置的判断积木");
            i+=1;
# 相同 无意义
def jcjm01(jmwz,srks,srjs):
    global j,jg,i,m;
    # print(require("util").inspect(String,True,null))
    j=indexof(jcjm0101,jcjmlxdq);
    if(j!=-1):
        if(j%5==2 or j%5==3):
            jg=sjsz[srks+1];
            if(jg>0 and jg<=1000000):
                if("#"+sjmz[jg]==jcjm0101[j-2]):
                    jcjgzj(jmwz,"2无意义的积木");
        if(j%5==1 or j%5==4):
            jcjmsrsz(jmwz,sjsz[srks+1],"0","2无意义的积木");
        i=jmwz;
        while(True):
            if(sjsz[sjwz[i]]==0):
                return;
            jg=jcjm0101[Math.floor(j/5)*5];
            if(jg=="#v"):
                jcjmssjm(i,sjsz[srks+2]-1000000,True,i);
                if(jg!=0):
                    return;
            else:
                if(jg!="#" and jg!="#!"):
                    jcjmssjm(i,jg,True,i);#m
                    if(jg!=0):
                        return;
            i=sjsz[sjwz[i]];
            m=indexof(jcjm0101,sjmz[i]);
            if(m==-1):
                if(not includes(jcjm0102,sjmz[i])):
                    return;
            else:
                jg=0;
                if(Math.floor(j/5)==Math.floor(m/5)):
                    jg=1;
                    if(jcjm0101[Math.floor(j/5)*5]=="#v"):
                        # print(j,m,i,sjsz[sjwz[i]+2],sjsz[srks+2])
                        if(sjsz[sjwz[i]+2]!=sjsz[srks+2]):
                            jg=0;
                    else:
                        if(jcjm0101[Math.floor(j/5)*5]=="#!"):
                            if(j%5<=2 and m%5<=2):
                                # print(j,m,i,sjwb[-sjsz[sjwz[i]+2]-1],sjwb[-sjsz[srks+2]-1])
                                if(sjwb[-sjsz[sjwz[i]+2]-1]
                                !=sjwb[-sjsz[srks+2]-1]):
                                    jg=0;
                    if(j%5==3 and (m%5==1 or m%5==4)):
                        jg=0;
                else:
                    if(j<5 and m<15 or j<15 and m<5):
                        jg=1;
            if(jg==1):
                jcjgzj(jmwz,"3相同功能的积木");
                jcjgzj(i,":和这个相同");
                return;
    else:
        j=indexof(jcjm0102,jcjmlxdq);
        if(j!=-1):
            i=jmwz;
            while(True):
                if(sjsz[sjwz[i]]==0):
                    return;
                i=sjsz[sjwz[i]];
                if(jcjmlxdq==sjmz[i]):
                    jcjgzj(jmwz,"3相同功能的积木");
                    jcjgzj(i,":和这个相同");
                    return;
                else:
                    if(not includes(jcjm0101,sjmz[i])):
                        return;
# 效果范围
def jcjm02(jmwz,srks,srjs):
    global i,m;
    if(jcjmlxdq=="looks_seteffectto"):
        i=sjsz[srks+1];
        if(i<0 and i>=-1000000):
            i=Number(sjwb[-i-1]);
            m=sjsz[srks+2];
            if(m=="COLOR"):
                if(i<0 or i>=200):
                    jcjgzj(jmwz,"1效果颜色值超出范围(0到200)");
            if(m=="FISHEYE"):
                if(i<0):
                    jcjgzj(jmwz,"1效果鱼眼值超出范围(不能小于0)");
            if(m=="WHIRL"):
                if(False):
                    jcjgzj(jmwz,"1效果漩涡值超出范围()");
            if(m=="PIXELATE"):
                if(i<0):
                    jcjgzj(jmwz,"1效果像素化值超出范围(不能小于0");
            if(m=="MOSAIC"):
                if(i<0 and i%10!=0):
                    jcjgzj(jmwz,"1效果马赛克值不在范围(10的倍数)");
            if(m=="BRIGHTNESS"):
                if(Math.abs(i)>100):
                    jcjgzj(jmwz,"1效果亮度值超出范围(-100到100)");
                if(Math.abs(i)<1):
                    jcjgzj(jmwz,"3效果亮度值可能太小(-100到100)");
            if(m=="GHOST"):
                if(i<0 or i>100):
                    jcjgzj(jmwz,"1效果虚像值超出范围(0到100)");
                else:
                    if(i<1):
                        jcjgzj(jmwz,"3效果虚像值可能太小(0到100)");
        return;
    if(jcjmlxdq=="sound_seteffectto"):
        i=sjsz[srks+1];
        if(i<0 and i>=-1000000):
            i=Number(sjwb[-i-1]);
            m=sjsz[srks+2];
            if(m=="PITCH"):
                if(Math.abs(i)>1000):
                    jcjgzj(jmwz,"1效果音调值超出范围(-1000到1000)");
                if(Math.abs(i)<8):
                    jcjgzj(jmwz,"1效果音调值可能太小(100为八度)");
            if(m=="PAN"):
                if(Math.abs(i)>100):
                    jcjgzj(jmwz,"1效果左右平衡值超出范围(-100到100)");
                if(Math.abs(i)<5):
                    jcjgzj(jmwz,"1效果左右平衡值可能太小(-100到100)");
        return;
# 循环 如果 克隆 停止
def jcjm03(jmwz,srks,srjs):
    global i,m,j,jg;
    if(jcjmlxdq=="control_forever"):
        jcjm03xh(sjsz[srks+1]);
    if(jcjmlxdq=="control_repeat"
     or jcjmlxdq=="control_repeat_until"
     or jcjmlxdq=="control_while"
     or jcjmlxdq=="control_for_each"):
        jcjm03xh(sjsz[srks+2]);
    if(jcjmlxdq=="control_repeat"
     or jcjmlxdq=="control_for_each"):
        i=sjsz[srks+1];
        if(i<0 and i>=-1000000):
            m=Number(sjwb[-i-1]);
            if(m<=0 or m%1!=0):
                jcjgzj(jmwz,"0重复执行次数不是正整数");
            if(m>100000000):
                jcjgzj(jmwz,"3重复执行次数太多");
        return;
    if(jcjmlxdq=="control_wait"):
        i=sjsz[srks+1];
        if(i<0 and i>=-1000000):
            m=Number(sjwb[-i-1]);
            if(m<0):
                jcjgzj(jmwz,"0等待负数秒");
            if(m>300):
                jcjgzj(jmwz,"3等待时间太久(超过5分钟)");
        return;
    if(jcjmlxdq=="control_if"):
        i=sjsz[srks];
        if(i>0 and i<=1000000):
            m=sjmz[i];
            if(m=="control_if"
             or m=="control_if_else"):
                jcjmblgb(sjsz[srks+1],sjsz[srks+2],i);#m
                if(jg!=0):
                    # print(i,sjwz[i]+1)#m
                    jcjmblgb(sjsz[sjwz[i]+1],sjsz[srks+2],i);#m
                    if(jg!=0):
                        i=sjsz[srks+2];
                        while(sjsz[sjwz[i]]!=0):
                            i=sjsz[sjwz[i]];
                        j=1;
                        if(sjmz[i]=="control_stop"):
                            i=sjsz[sjwz[i]+1];
                            if(sjwb[-i-1]=="this script"):
                                j=0;
                            else:
                                if(sjwb[-i-1]=="all"):
                                    j=0;
                        if(j==1):
                            jcjgzj(jg,"3如果积木内的积木可能会干扰下一个如果积木的条件");
                            jcjgzj(jmwz,":这个如果积木");
                            jcjgzj(sjsz[srks],":下一个如果积木");
        return;
    if(jcjmlxdq=="control_while"
     or jcjmlxdq=="control_repeat_until"):
        # print(srks,len(sjsz))#m
        jcjmblgb(sjsz[srks+1],sjsz[srks+2],i);
        if(jg==0):
            jcjmwtbl(sjsz[srks+1],i);
            if(jg==0):
                jcjgzj(jmwz,"3循环条件没在循环体中改变");
            else:
                jcjgzjyb(jmwz,"3循环条件没在循环体中改变");
        else:
            if(jcjmlxdq=="control_while"):
                jcjmblfx(sjsz[srks+1],sjsz[srks+2],1,i);
            else:
                jcjmblfx(sjsz[srks+1],sjsz[srks+2],-1,i);
        return;
    if(jcjmlxdq=="control_create_clone_of"):
        i=sjsz[srks+1];
        if(sjmz[i]=="control_create_clone_of_menu"):
            i=sjsz[sjwz[i]+1];
            if(sjwb[-i-1]=="_myself_"):
                i=sjmz[jcjmktdq];
                if(contains(i,"_when")
                 and i!="event_whenflagclicked"
                 or i=="control_start_as_clone"):
                    i=0;
                    jg=0;
                    # print("kelong",jcjmlb);
                    while(i<len(jcjmlb) and jg==0):
                        if(sjmz[jcjmlb[i]]=="control_if"
                         or sjmz[jcjmlb[i]]=="control_if_else"):
                            jcjmjsbl(jcjmlb[i],i);
                        i+=2;
                    if(jg==0):
                        jcjgzj(jmwz,"3克隆操作没有局部变量控制");
        return;
    if(jcjmlxdq=="control_delete_this_clone"):
        i=0;
        jg=0;
        while(i<len(jcjmlb) and jg==0):
            if(sjsz[sjwz[jcjmlb[i]]]!=0):
                jg=jcjmlb[i];
            i+=2;
        if(jg!=0):
            jcjgzj(jmwz,"3删除克隆体积木后仍有可被运行的积木");
            jcjgzj(sjsz[sjwz[jg]],":在这里");
            jcjgzj(jg,":因为有这个积木");
    if(jcjmlxdq=="control_stop"):
        i=sjsz[srks+1];
        if(sjwb[-i-1]=="this script"):
            if(jcdywzdq!=-1):
                jcjgzj(jmwz,"4在自定义积木中停止这个脚本只会跳出自定义积木");
                jcjgzj(jcjmktdq,":在这里");
        if(sjwb[-i-1]=="this script"
         or sjwb[-i-1]=="all"):
            i=len(jcjmlb)-2;
            if(len(jcjmlb)<2
             or sjmz[jcjmlb[i]]!="control_if"
             and sjmz[jcjmlb[i]]!="control_if_else"):
                jcjgzj(jmwz,"2停止积木应该被放在如果/那么积木的后面");
                if(len(jcjmlb)>=2):
                    jcjgzj(jcjmlb[i],":但是它在这个积木的末尾");
                else:
                    jcjgzj(jcjmktdq,":但是它在这个积木的末尾");
# 检查循环体
def jcjm03xh(jmwz):
    global jg,i;
    if(jmwz>0 and jmwz<=1000000):
        if(sjsz[sjwz[jmwz]+1]==0):
            if(sjmz[jmwz]=="sound_play"):
                jcjgzj(jmwz,"1应使用'播放声音并等待'");
        if(jcjmyb==0):
            jg=0;
            i=0;
            while(i<len(jcjm0302) and jg==0):
                jcjmssjm(jmwz,jcjm0302[i],False,i);
                i+=1;
            while(i<len(jcjm0004) and jg==0):
                jcjmssjm(jmwz,jcjm0004[i],False,i);
                i+=1;
            if(jg==0):
                jcjgzjyb(jmwz,"3建议使用'运行时不刷新屏幕'");
# 侦测 计算 变量 画笔
def jcjm04(jmwz,srks,srjs):
    global i,jg,j,m;
    if(jcjmlxdq=="sensing_dayssince2000"):
        jcjgzj(jmwz,"4注意时区差异");
        return;
    if(jcjmlxdq=="sensing_current"):
        if(sjwb[-sjsz[srks+1]-1]=="DAYOFWEEK"):
            jcjgzj(jmwz,"4注意星期差异");
        return;
    if(jcjmlxdq=="sensing_of_object_menu"):
        if(sjwb[-sjsz[srks+1]-1]=="_stage_"):
            jcjgzj(jmwz,"2无意义的积木(可以用更简单的积木替换");
        return;
    clwbqm2("operator_",jcjmlxdq);
    if(clwbwz==-1):
        if(jcjmlxdq=="operator_not"):
            i=0;
            while(i<len(jcjmlb)):
                if(sjmz[jcjmlb[i]]=="operator_not"):
                    jcjgzj(jcjmlb[i],"3不成立里包含不成立");
                    jcjgzj(jmwz,":包含的不成立");
                i+=2;
        jg=0;
        i=srks+1;
        while(i<srjs):
            if(sjsz[i]>0 or sjsz[i]<-1000000):
                jg=1;
            if(jcjmlxdq!="operator_equals"):
                jcjmsrsz(jmwz,sjsz[i],"","2空白的操作数");
            if(jcjmlxdq=="operator_add"):
                jcjmsrsz(jmwz,sjsz[i],"0","3加零");
            if(jcjmlxdq=="operator_subtract" and i-srks==2):
                jcjmsrsz(jmwz,sjsz[i],"0","3减零");
            if(jcjmlxdq=="operator_multiply"):
                jcjmsrsz(jmwz,sjsz[i],"0","2乘零");
                jcjmsrsz(jmwz,sjsz[i],"1","3乘一");
            if(jcjmlxdq=="operator_divide"
             or jcjmlxdq=="operator_mod"):
                if(i-srks==2):
                    jcjmsrsz(jmwz,sjsz[i],"0","2被零除");
                    jcjmsrsz(jmwz,sjsz[i],"1","3除一");
                else:
                    jcjmsrsz(jmwz,sjsz[i],"0","3除零");
            if(jcjmlxdq=="operator_letter_of" and i-srks==2):
                j=sjsz[i];
                if(j<0 and j>=-1000000):
                    m=Number(sjwb[-j-1]);
                    if(m<=0 or m%1!=0):
                        jcjgzj(jmwz,"0字符编号不大于0");
            if(jcjmlxdq=="operator_equals"):
                j=sjsz[i];
                if(j<0 and j>=-1000000):
                    m=sjwb[-j-1];
                    if(not isNaN(m) and m!="" and Number(m)%1!=0):
                        jcjgzj(jmwz,"2用等于号比较小数");
                    jcwbdx(m);
                    if(clwbwz==-1):
                        jcjgzj(jmwz,"4比较不区分大小写");
            i+=1;
        if(jg==0):
            if(jcjmlxdq!="operator_random"
             and jcjmlxdq!="operator_mathop"):
                jcjgzj(jmwz,"2无意义的积木");
        return;
    if(jcjmlxdq=="data_insertatlist"
     or jcjmlxdq=="data_replaceitemoflist"
     or jcjmlxdq=="data_deleteoflist"
     or jcjmlxdq=="data_itemoflist"):
        m=sjsz[srks+1];
        if(m<0 and m>=-1000000):
            m=sjwb[-m-1];
            if(not isNaN(m) and m!="" and (Number(m)<=0 or Number(m)%1!=0)):
                jcjgzj(jmwz,"0项目编号不大于0");
    if(jcjmlxdq=="pen_setPenColorParamTo"):
        m=Number(sjsz[srks+1]);
        if(m<0 and m>=-1000000):
            m=Number(sjwb[-m-1]);
            if(m<0 or m>100):
                jcjgzj(jmwz,"2画笔参数应在0到100之间");
# ] 检查工具 [
# 检查积木1是否有变量在积木2中被改变
def jcjmblgb(jm1,jm2,ii):
    global jg,i,m,j;
    # print("jcjmblgb")
    jg=0;
    if(jm1>0 and jm1<=1000000):
        # print(i,jm1,sjmz[jm1-5:jm1+5])#m
        i=indexof(jcjm0101,"#"+sjmz[jm1]);
        if(i!=-1):
            i+=1;
            while(jcjm0101[i][0]!="#" and jg==0):
                jcjmssjm(jm2,"#"+jcjm0101[i],False,i);
                i+=1;
        i=sjwz[jm1]+1;
        while(i<sjwz[jm1+1] and jg==0):
            m=sjsz[i];
            if(m>1000000 and m<=2000000):
                j=m+1000000;
            else:
                if(m<-1000000 and m>=-2000000):
                    j=m-1000000;
                else:
                    if(Math.abs(m)>1000000 and Math.abs(m)<=2000000):
                        j=m;
                    else:
                        j=0;
            if(j==0):
                jcjmblgb(m,jm2,i);
            else:
                jcjmssjm(jm2,j,False,i);
            i+=1;
    i=ii;

# 检查积木是否改变指定变量/是否有指定积木,hlhm忽略后面拼接的积木
def jcjmssjm(jmwz,wz,hlhm,ii):
    global i,jcjm03dy;
    i=0;
    jcjm03dy=[];
    while(i<len(jcdywz)):
        jcjm03dy.append(0);
        i+=1;
    i=ii;
    jcjmssj1(jmwz,wz,hlhm,i);

def jcjmssj1(jmwz,wz,hlhm,ii):
    global jg,i,m;
    # print("jcjmssj1")
    jg=0;
    if(jmwz>0 and jmwz<=1000000):
        if("#"+sjmz[jmwz]==wz):
            jg=jmwz;
        else:
            i=sjwz[jmwz];
            if(hlhm):
                i+=1;
            while(i<sjwz[jmwz+1] and jg==0):
                m=sjsz[i];
                if(m==wz):
                    if(includes(jcjm0314,sjmz[jmwz])):
                        jg=jmwz;
                else:
                    jcjmssj1(m,wz,False,i);
                i+=1;
    else:
        if(jmwz>3000000):
            m=jmwz-3000001;
            if(jcjm03dy[m]==0):
                jcjm03dy[m]=1;
                if(jcdywz[m]!=0):
                    m=Math.abs(jcdywz[m]);
                    jcjmssj1(sjsz[sjwz[m]],wz,False,i);
    i=ii;

# 检查积木1的变量在积木2中改变方向不正确
def jcjmblfx(jm1,jm2,fx,ii):
    global jcjm03wz,i,j,m;
    jcjm03wz=[];
    jcjm03wz.append(jm1);
    # print("jcjmblfx",jm1)
    if(jm1>0 and jm1<=1000000):
        i=indexof(jcjm0101,"#"+sjmz[jm1]);
        if(i!=-1):
            # print("jcjmblfx",jcjm0101.slice(i+1,4))
            jcjmssfx(jm2,"#"+jcjm0101[i+1],fx,i);
            jcjmssfx(jm2,"#"+jcjm0101[i+2],0,i);
            jcjmssfx(jm2,"#"+jcjm0101[i+3],0,i);
            jcjmssfx(jm2,"#"+jcjm0101[i+4],-fx,i);
        i=sjwz[jm1]+1;
        while(i<sjwz[jm1+1]):
            j=sjsz[i];
            if(j>1000000 and j<=2000000):
                j=j+1000000;
            else:
                if(j<-1000000 and j>=-2000000):
                    j=j-1000000;
                else:
                    j=0;
            m=fx;
            if(sjmz[jm1]=="operator_gt" and i==sjwz[jm1]+2):
                m=-m;
            if(sjmz[jm1]=="operator_lt" and i==sjwz[jm1]+1):
                m=-m;
            if(sjmz[jm1]=="operator_not"):
                m=-m;
            if(sjmz[jm1]=="operator_equals"):
                m=2;
            if(j==0):
                jcjmblfx(sjsz[i],jm2,m,i);
            else:
                # print("jcjmblfx",j,m)
                jcjmssfx(jm2,j,m,i);
            i+=1;
    i=ii;

# 检查指定积木反方向改变变量
def jcjmssfx(jmwz,wz,fx,ii):
    global i,jcjm03dy;
    # print("jcjmssfx",jm1)
    i=0;
    jcjm03dy=[];
    while(i<len(jcdywz)):
        jcjm03dy.append(0);
        i+=1;
    i=ii;
    jcjmssf1(jmwz,wz,fx,i);

def jcjmssf1(jmwz,wz,fx,ii):
    global jg,m,i;
    # print("jcjmssf1",jmwz,wz,fx)
    if(wz=="#"):
        return;
    jg=0;
    if(jmwz>0 and jmwz<=1000000):
        # print("jcjmssfx",jmwz,"#"+sjmz[jmwz])
        if("#"+sjmz[jmwz]==wz):
            m=sjsz[sjwz[jmwz]+1];
            if(m<0 and m>=-1000000):
                if(fx==0):
                    jg="3循环变量在循环内被初始化";
                else:
                    if(Math.abs(fx)==1):
                        m=Number(sjwb[-m-1]);#m
                        if(m*fx>0):#m
                            jg="3循环变量改变方向不正确";
        else:
            i=sjwz[jmwz];
            while(i<sjwz[jmwz+1] and jg==0):
                m=sjsz[i];
                # print("jcjmssfx",sjwz[jmwz],i,m)
                if(m==wz):
                    jg=jmwz;
                else:
                    jcjmssf1(m,wz,fx,i);
                i+=1;
            if(jg!=0):
                jg=0;
                if(sjmz[jmwz]=="data_setvariableto"):
                    m=sjsz[sjwz[jmwz]+1];
                    if(m<0 and m>=-1000000):
                        jg="3循环变量在循环内被初始化";
                else:
                    if(sjmz[jmwz]=="data_changevariableby"):
                        m=sjsz[sjwz[jmwz]+1];
                        if(m<0 and m>=-1000000 and Math.abs(fx)==1):
                            m=Number(sjwb[-m-1]);#m
                            # print("jcjm0322change",m)
                            if(m*fx>0):#m
                                jg="3循环变量改变方向不正确";
        if(jg!=0):
            i=len(jcjm03wz)-1;
            if(i>0):
                jcjgzj1(jmwz,jcjm03wz[i],jg);
            else:
                jcjgzj(jmwz,jg);
            while(i>0):
                jcjgzj1(jcjm03wz[i],jcjm03wz[i],":来自定义");
                i-=1;
            jcjgzj1(jcjm03wz[0],jcjmktdq,":循环条件");
    else:
        if(jmwz>3000000):
            m=jmwz-3000001;
            if(jcjm03dy[m]==0):
                jcjm03dy[m]=1;
                if(jcdywz[m]!=0):
                    m=Math.abs(jcdywz[m]);
                    jcjm03wz.append(jmwz);
                    jcjmssf1(sjsz[sjwz[m]],wz,fx,i);
                    jcjm03wz.pop();
    i=ii;

# 检查积木的数值是否为wz的数值，如果是则提示文本
def jcjmsrsz(jmwz,wz,sz,wb):
    global m;
    if(wz<0 and wz>=-1000000):
        m=sjwb[-wz-1];
        if(m==sz
         or  not isNaN(m)
         and  not isNaN(sz)
         and m!=""
         and sz!=""
         and Number(m)==Number(sz)
        ):
            jcjgzj(jmwz,wb);
# 检查积木(是否有)角色变量
def jcjmjsbl(jmwz,ii):
    global jg,i,m;
    jg=0;
    if(jmwz>0 and jmwz<=1000000):
        i=sjwz[jmwz];
        while(i<sjwz[jmwz+1] and jg==0):
            m=sjsz[i];
            if(m>1000000 and m<=3000000):
                jg=jmwz;
            else:
                jcjmjsbl(m,i);
            i+=1;
    i=ii;

# 检查积木(是否有)舞台变量(包括类似 x坐标)
def jcjmwtbl(jmwz,ii):
    global jg,i,m;
    jg=0;
    if(jmwz>0 and jmwz<=1000000):
        i=sjmz[jmwz];
        clwbqm2("operator_",i);
        if(clwbwz!=-1):
            clwbqm2("data_",i);
            if(clwbwz!=-1):
                clwbqm2("argument_",i);
                if(clwbwz!=-1):
                    if(i!="sensing_distanceto"
                     and i!="sensing_touchingobject"
                     and i!="sensing_touchingcolor"
                     and i!="sensing_coloristouchingcolor"):
                        jg=-1;
        i=sjwz[jmwz];
        while(i<sjwz[jmwz+1] and jg==0):
            m=sjsz[i];
            if(m<-1000000 and m>=-3000000):
                jg=jmwz;
            else:
                jcjmwtbl(m,i);
            i+=1;
    i=ii;

def jcwbdx(st):
    global clwbwz;
    # $c=x;
    clwbwz=0;
    while(clwbwz<len(st)):
        if(contains("ABCDEFGHIJKLMNOPQRSTUVWXYZ",st[clwbwz])):
            clwbwz=-1;
            return;
        clwbwz+=1;
def jcks():
    global jcjm0001,jcjm0002,jcjm0003,jcjm0004,jcjm0101,jcjm0102,jcjm0302,jcjm0314;
    # 使用变量的积木
    jcjm0001=[
        "data_listcontainsitem",
        "data_itemnumoflist",
        "data_itemoflist",
        "data_showlist",
        "data_showvariable",
        "data_savelist",
        "data_savevariable"
    ];
    # 判断积木
    jcjm0002=[
        "sensing_touchingobject",
        "sensing_coloristouchingcolor",
        "sensing_touchingcolor",
        "sensing_keypressed",
        "sensing_mousedown",
        "operator_contains",
        "operator_and",
        "operator_or",
        "operator_not",
        "data_listcontainsitem",
        "sensing_loud",
        "community_isMyFans",
        "community_isLiked",
        "faceSensing_faceIsDetected",
        "community_isFollower",
        "community_isProjectLover",
        "puzzle_isPaintSameAsWatermark"
    ];
    # 带有判断条件的积木
    jcjm0003=[
        "operator_and",
        "operator_or",
        "operator_not",
        "control_if",
        "control_if_else",
        "control_repeat_until",
        "control_while",
        "control_wait_until"
    ];
    # 导致等待的积木
    jcjm0004=[
        "music_playDrumForBeats",
        "music_restForBeats",
        "music_playNoteForBeats",
        "looks_sayforsecs",
        "looks_thinkforsecs",
        "data_savevariable",
        "data_savelist",
        "data_loadvariable",
        "data_loadlist",
        "text_animateText"
    ];
    # 变量与会影响他们的积木(1.增加 2.设定 3.影响 4.减少)
    jcjm0101=[
        "#position",# 0
        "",
        "motion_gotoxy",
        "motion_goto",
        "",
        "#motion_xposition",
        "motion_changexby",
        "motion_setx",
        "",
        "",
        "#motion_yposition",
        "motion_changeyby",
        "motion_sety",
        "",
        "",
        "#motion_direction",
        "motion_turnright",
        "motion_pointindirection",
        "motion_pointtowards",
        "motion_turnleft",
        "#looks_costumenumbername",
        "looks_nextcostume",
        "looks_switchcostumeto",
        "",
        "",
        "#looks_backdropnumbername",
        "looks_nextbackdrop",
        "looks_switchbackdropto",
        "",
        "",
        "#looks_size",
        "looks_changesizeby",
        "looks_setsizeto",
        "",
        "",
        "#",
        "",
        "looks_show",
        "looks_hide",
        "",
        "#",
        "looks_gotofrontback",
        "looks_goforwardbackwardlayers",
        "",
        "",
        "#!",
        "looks_changeeffectby",
        "looks_seteffectto",
        "looks_cleargraphiceffects",
        "",
        "#sound_volume",
        "sound_changevolumeby",
        "sound_setvolumeto",
        "",
        "",
        "#!",
        "sound_changeeffectby",
        "sound_seteffectto",
        "sound_cleareffects",
        "",
        "#v",
        "data_changevariableby",
        "data_setvariableto",
        "",
        "",
        "#!",
        "pen_changePenColorParamBy",
        "pen_setPenColorParamTo",
        "pen_setPenColorToColor",
        "",
        "#",
        "pen_changePenSizeBy",
        "pen_setPenSizeTo",
        "",
        "",
        "#music_getTempo",
        "music_changeTempo",
        "music_setTempo",
        "",
        ""
    ];
    # 不能重复使用的积木
    jcjm0102=[
        "motion_setrotationstyle",
        "motion_ifonedgebounce",
        "motion_movesteps",
        "sensing_setdragmode",
        "sensing_resettimer",
        "music_setInstrument",# 5
        "videoSensing_videoToggle",
        "text2speech_setVoice",
        "text2speech_setLanguage",
        "control_clear_counter",
        "text_setText",# 10
        "text_setFont",
        "text_setColor",
        "text_setWidth",
        "",
    ];
    # 导致画面变化的积木
    jcjm0302=[
        "looks_say",
        "looks_switchcostumeto",
        "looks_nextcostume",
        "looks_switchbackdropto",
        "looks_nextbackdrop",
        "looks_changesizeby",
        "looks_setsizeto",
        "looks_changeeffectby",
        "looks_seteffectto",
        "looks_cleargraphiceffects",
        "looks_show",
        "looks_hide",
        "looks_gotofrontback",
        "looks_goforwardbackwardlayers",
        "motion_movesteps",
        "motion_turnright",
        "motion_turnleft",
        "motion_goto",
        "motion_gotoxy",
        "motion_pointindirection",
        "motion_pointtowards",
        "motion_changexby",
        "motion_setx",
        "motion_changeyby",
        "motion_sety",
        "motion_ifonedgebounce",
        "box2d_doTick",
        "text_clearText",
        "text_setFont",
        "text_setColor",
        "text_setWidth",
        "motion_movegrids",
        "pen_stamp",
        "pen_penDown",
    ];
    # 导致变量改变的积木
    jcjm0314=[
        "data_loadvariable",
        "data_loadlist",
        "data_setvariableto",
        "data_changevariableby",
        "data_addtolist",
        "data_deleteoflist",
        "data_deletealloflist",
        "data_insertatlist",
        "data_replaceitemoflist"
    ];

# ]
# ]
def contains(a,b):
    try:
        a.index(b);
        return True;
    except:
        return False;
def indexof(a,b):
    try:
        return a.index(b);
    except:
        return -1;
def includes(a,b):
    try:
        a.index(b);
        return True;
    except:
        return False;

class __Math():
    def abs(this,x):
        return x.__abs__();
    def floor(this,x):
        return int(x);

def Number(x):
    try:
        return int(x);
    except:
        try:
            return float(x);
        except:
            return 1e1000;

def String(x):
    return str(x);

def isNaN(x):
    try:
        return float(x)==1e1000;
    except:
        return True;

Math = __Math();

start();
