#!/usr/bin/env python
#-*- coding:utf-8 -*-

from growl import GrowlPing
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.api import get_latest_build

import settings
import time

if __name__ == '__main__':
    while True:
        je = Jenkins(settings.JENKINS_URL)
        
        jobs_list = je.get_jobs_list()
        
        jobs_broken = []
        
        for job_name in jobs_list:
            
            last_build = get_latest_build(settings.JENKINS_URL, job_name)
            
            if not last_build.is_good():
                jobs_broken.append(job_name)
                
        if jobs_broken:
            p = GrowlPing()
            p.notify(jobs_broken)
        
        time.sleep(300)