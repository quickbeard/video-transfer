#!/bin/bash
sudo ovs-vsctl add Bridge s1 flow_tables 0=@ft -- --id=@ft create Flow_Table flow_limit=5 overflow_policy=refuse
for ((i=1; i <= 253; ++i))
do
    sudo ovs-vsctl add bridge s1 flow_tables $i=@ft -- --id=@ft create Flow_Table flow_limit=1 overflow_policy=refuse
done