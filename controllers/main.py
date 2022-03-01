
import os
import sys
from flask import jsonify,render_template,send_file, request,flash, redirect ,url_for,session,send_file, Blueprint,request
import time
import datetime
import json
import boto3
from collections import defaultdict
from helpers.sib_meta import *
from helpers.meta_create import *
from helpers.meta_extract import *
from helpers.forms import *
from jinja2.exceptions import TemplateNotFound

boto3.setup_default_session(profile_name='sib')
dynamodb = boto3.resource('dynamodb')
meta_table = dynamodb.Table('sibylity_fcr_metadata')

index = Blueprint('index', __name__)

@index.route('/',methods=['GET','POST'])
def dashboard():
    try:
        metadata = get_metadata(meta_table)
        return render_template(
            'list.html',
            metadata = metadata,
            list_title="Metadata",
            active_page="dashboard"
        )
    except TemplateNotFound:
        abort(404)
    return 


@index.route('/settings',methods=['GET','POST'])
def settings():
    try:
        metadata = get_settings_metadata(meta_table)
        return render_template(
            'settings/list.html',
            metadata = metadata,
            list_title="Settings",
            active_page="settings",
        )
    except TemplateNotFound:
        abort(404)
    return 


@index.route('/threats',methods=['GET','POST'])
def threats():
    try:
        metadata = get_threats_metadata(meta_table)
        return render_template(
            'threats/list.html',
            metadata = metadata,
            list_title="Threats",
            active_page="threats",
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/scope',methods=['GET','POST'])
def project_scope_settings():
    try:
        metadata = get_project_scope_settings_metadata(meta_table)
        return render_template(
            'list.html',
            metadata = metadata,
            list_title="Project Scope Settings",
            active_page="scope",
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/control-families',methods=['GET','POST'])
def control_families():
    try:
        metadata = get_control_families_metadata(meta_table)
        return render_template(
            'control_families/list.html',
            metadata = metadata,
            list_title="Control Families",
            active_page="families",
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/controls',methods=['GET','POST'])
def controls():
    try:
        vulnerabilities = get_vulnerabilities_metadata(meta_table)
        controls = get_controls_metadata(meta_table)
        vulnerabilities = sorted(vulnerabilities, key=lambda d: d['id'])
        controls = sorted(controls, key=lambda d: d['id'])
        
        return render_template(
            'controls/list.html',
            controls = controls,
            vulnerabilities = vulnerabilities,
            list_title="Vulnerabilities and Controls",
            active_page="controls",
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/valuesets',methods=['GET','POST'])
def valuesets():
    try:
        metadata = get_valuesets_metadata(meta_table)
        return render_template(
            'valuesets/list.html',
            metadata = metadata,
            list_title="Valuesets",
            active_page="valuesets",
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/create-control',methods=['GET','POST'])
def create_control():

    try:
        metadata = get_metadata(meta_table)
        control_families = [x['key'] for x in  metadata if x['class']== "control_family"]
        threats = [x['key'] for x in  metadata if x['class'] == "threat"]
                

        if request.method == 'POST':
            form = request.form
            control = extract_control(form)
            vulnerability = extract_vulnerability(form,threats)
            success1 = ddb_create_control(meta_table,control)
            if success1:
                success2 = ddb_create_vulnerability(meta_table,vulnerability)
            if success1 and success2:
                return redirect(url_for('index.controls'))
            
        return render_template(
            'controls/create.html',
            control_families = control_families,
            threats = threats
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/create-settings',methods=['GET','POST'])
def create_settings():
    try:
        if request.method == 'POST':
            form = request.form
            settings = extract_settings(form)
            success = ddb_create(meta_table,settings)
            print(success)
            if success:
                return redirect(url_for('index.settings'))
            
        return render_template(
            'settings/create.html',
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/create-threat',methods=['GET','POST'])
def create_threat():
    try:
        if request.method == 'POST':
            form = request.form
            threat = extract_threat(form)
            success = ddb_create_threat(meta_table,threat)
            print(success)
            if success:
                return redirect(url_for('index.threats'))
            
        return render_template(
            'threats/create.html',
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/create-control-family',methods=['GET','POST'])
def create_control_family():
    try:
        if request.method == 'POST':
            form = request.form
            cf = extract_control_family(form)
            success = ddb_create_control_family(meta_table,cf)
            print(success)
            if success:
                return redirect(url_for('index.control_families'))
            
        return render_template(
            'control_families/create.html',
        )
    except TemplateNotFound:
        abort(404)
    return


@index.route('/create-valueset',methods=['GET','POST'])
def create_valueset():
    try:
        if request.method == 'POST':
            form = request.form
            vs = extract_valueset(form)
            success = ddb_create_control_family(meta_table,vs)
            if success:
                return redirect(url_for('index.valuesets'))
            print(success)
            
        return render_template(
            'valuesets/create.html',
        )
    except TemplateNotFound:
        abort(404)
    return




