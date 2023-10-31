Service Data Model as Input to AW-SDX
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Layer 2 VPN Service Model
^^^^^^^^^^^^^^^^^^^^^^^^^

“The YANG data model defined in this document includes support for

point-to-point Virtual Private Wire Services (VPWSs) and multipoint

Virtual Private LAN Services (VPLSs) that use Pseudowires signaled

using the Label Distribution Protocol (LDP) and the Border Gateway

Protocol (BGP) as described in RFCs 4761 and 6624.”
(https://datatracker.ietf.org/doc/html/rfc8466)

1. .. rubric:: Point-to-point Virtual Private Wire Services (VPWSs)
      :name: point-to-point-virtual-private-wire-services-vpwss

2. .. rubric:: Multipoint Virtual Private LAN Services (VPLSs)
      :name: multipoint-virtual-private-lan-services-vplss

Layer 3 IP VPN service
^^^^^^^^^^^^^^^^^^^^^^

   It is a collection of sites that are authorized to exchange traffic
   between each other over a shared IP infrastructure.”
   (https://www.rfc-editor.org/rfc/rfc8299.html)

   The YANG module is divided into two main containers: "vpn-services"
   and "sites". Authorization of traffic exchange is done through what
   we call a VPN policy or VPN service topology defining routing
   exchange rules between sites. The type of VPN service topology is
   required for configuration. Our proposed model supports any-to-any,
   Hub and Spoke (where Hubs can exchange traffic), and "Hub and Spoke
   disjoint" (where Hubs cannot exchange traffic).

   A Layer 3 PE-based VPN is built using route targets (RTs) as
   described in [`RFC4364 <https://www.rfc-editor.org/rfc/rfc4364>`__].

1. .. rubric:: Multi-AS Backbones
      :name: multi-as-backbones

   1. VRF-to-VRF connections at the AS (Autonomous System) border
         routers. Two neighboring PE routers are directly attached.

   2. EBGP redistribution of labeled VPN-IPv4 routes from AS to
         neighboring AS.

   3. Multi-hop EBGP redistribution of labeled VPN-IPv4 routes between
         source and destination ASes, with EBGP redistribution of
         labeled IPv4 routes from AS to neighboring AS.
