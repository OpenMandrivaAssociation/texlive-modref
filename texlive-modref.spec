Name:		texlive-modref
Version:	1.0
Release:	1
Summary:	Customisation of cross-references in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/modref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package contains macros which allow authors to easily
customise how cross-references appear in their document, both
in general (across all cross-references) and for particular
types of references (identified by a prefix in the reference
label), in a very generic manner.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/modref/modref.sty
%doc %{_texmfdistdir}/doc/latex/modref/README
%doc %{_texmfdistdir}/doc/latex/modref/modref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/modref/modref.drv
%doc %{_texmfdistdir}/source/latex/modref/modref.dtx
%doc %{_texmfdistdir}/source/latex/modref/modref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
