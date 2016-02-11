#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Jeremiah Marks
# @Date:   2016-02-10 23:07:57
# @Last Modified 2016-02-10
# @Last Modified time: 2016-02-10 23:46:39

import AppointmentService
import BasicRequestHelper
import ClassService
import ClientService
import DebugPrinting
import FinderService
import SaleService
import SiteService
import StaffService

testcalls = ClientService.ClientServiceCalls()

print testcalls.GetAllClients()


