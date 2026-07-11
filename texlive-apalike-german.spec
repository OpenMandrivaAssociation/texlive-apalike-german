%global tl_name apalike-german
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A copy of apalike.bst with German localization
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/apalike-german
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike-german.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike-german.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A copy of apalike.bst (which is part of the base BibTeX distribution)
with German localization.

