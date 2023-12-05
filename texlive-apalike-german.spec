Name:		texlive-apalike-german
Version:	65403
Release:	1
Summary:	A copy of apalike.bst with German localization
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/apalike-german
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike-german.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/apalike-german.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A copy of apalike.bst (which is part of the base BibTeX
distribution) with German localization.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/apalike-german
%doc %{_texmfdistdir}/doc/bibtex/apalike-german

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
