


#Medium Resolution NHDplus
create table outgoing.medres_nhdplus_flow as
SELECT comid, gnis_id, reachcode, fcode, lengthkm,  the_geom_4269 as geom
from nhdplus.nhdflowlines
where fcode <> 56600;

