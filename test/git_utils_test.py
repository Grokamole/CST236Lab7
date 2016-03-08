'''
This file is made to test git_utils.py's functions.
'''
import sys
import datetime
import mock
import os
from unittest import TestCase
from utils.git_utils import is_file_in_repo, get_git_file_info, \
     has_diff_files, has_untracked_files, get_file_info, get_diff_files, \
     get_untracked_files, get_repo_root, get_repo_branch, get_repo_url, \
     git_execute

class TestGitUtils(TestCase):
    '''
    This class is used to test git_utils.py's functions.
    '''
    def test_invalid_path(self):
        self.assertRaises(Exception, get_git_file_info, "*.*")

    def test_valid_path(self):
        try:
            get_git_file_info("nose2.cfg")
            self.assertTrue(True)
        except Exception as exc:
            self.assertTrue(False)

    def test_file_in_repo(self):
        self.assertEqual(is_file_in_repo("nose2.cfg"), "Yes")

    def test_file_not_in_repo(self):
        self.assertEqual(is_file_in_repo("*.*"), "No")

    @mock.patch('utils.git_utils.get_diff_files')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_changed_untracked_repo(self, mock_ope, mock_get_diff):
        mock_ope.return_value = True
        mock_get_diff.return_value = os.path.abspath("test_untracked.txt")
        self.assertEqual(is_file_in_repo("test_untracked.txt"), "No")

    @mock.patch('utils.git_utils.os.path.exists')
    @mock.patch('utils.git_utils.get_diff_files')
    def test_get_git_fi_mod_locally(self, mock_get_diff, mock_ope):
        mock_get_diff.return_value = os.path.abspath("test_untracked.txt")
        mock_ope.return_value = True
        result = get_git_file_info("test_untracked.txt")
        self.assertEqual(result, "test_untracked.txt has been modified"+
                         " locally")

    @mock.patch('utils.git_utils.get_untracked_files')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_git_fi_not_checked(self, mock_ope, mock_get_diff):
        mock_ope.return_value = True
        mock_get_diff.return_value = os.path.abspath("test_untracked.txt")
        result = get_git_file_info("test_untracked.txt")
        self.assertEqual(result, "test_untracked.txt has been not been"+
                         " checked in")

    @mock.patch('utils.git_utils.get_diff_files')
    @mock.patch('utils.git_utils.get_untracked_files')
    @mock.patch('utils.git_utils.is_repo_dirty')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_git_fi_up_to_date(self, mock_ope, mock_ird, mock_guf, \
                                   mock_gdf):
        mock_ope.return_value = True
        mock_ird.return_value = False
        mock_guf.return_value = ""
        mock_gdf.return_value = ""
        result = get_git_file_info("test_untracked.txt")
        self.assertEqual(result, "test_untracked.txt is up to date")

    @mock.patch('utils.git_utils.has_diff_files')
    @mock.patch('utils.git_utils.has_untracked_files')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_is_repo_dirty_false(self, mock_ope, mock_huf, mock_hdf):
        mock_hdf.return_value = False
        mock_huf.return_value = False
        mock_ope.return_value = True
        result = get_git_file_info("test_untracked.txt")
        self.assertEqual(result, "test_untracked.txt is up to date")

    @mock.patch('utils.git_utils.os.path.exists')
    @mock.patch('utils.git_utils.get_diff_files')
    def test_does_not_have_diff_files(self, mock_gdf, mock_ope):
        mock_ope.return_value = True
        mock_gdf.return_value = ""
        self.assertEqual(False, has_diff_files("blah.txt"))

    @mock.patch('utils.git_utils.os.path.exists')
    @mock.patch('utils.git_utils.get_untracked_files')
    def test_has_untracked_files(self, mock_guf, mock_ope):
        mock_ope.return_value = True
        mock_guf.return_value = "greater than zero characters"
        self.assertEqual(True, has_untracked_files("blah.txt"))

    @mock.patch('utils.git_utils.os.path.exists')
    @mock.patch('utils.git_utils.get_untracked_files')
    def test_has_no_untracked_files(self, mock_guf, mock_ope):
        mock_ope.return_value = True
        mock_guf.return_value = ""
        self.assertEqual(False, has_untracked_files("blah.txt"))

    @mock.patch('utils.git_utils.git_execute')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_file_info(self, mock_ope, mock_ge):
        mock_ope.return_value = True
        mock_ge.return_value = "blah.txt"
        self.assertEqual("blah.txt", get_file_info("blah.txt"))

    @mock.patch('utils.git_utils.get_repo_root')
    @mock.patch('utils.git_utils.os.path.join')
    @mock.patch('utils.git_utils.os.path.normpath')
    @mock.patch('utils.git_utils.git_execute')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_diff_files(self, mock_ope, mock_ge, mock_opn, mock_opj, \
                            mock_grr):
        mock_ope.return_value = True
        mock_ge.side_effect = ["\n","1\n"]
        mock_opn.return_value = "1"
        mock_opj.return_value = ""
        mock_grr.return_value = ""
        self.assertEqual(["1"], get_diff_files("blah.txt"))

    @mock.patch('utils.git_utils.get_repo_root')
    @mock.patch('utils.git_utils.os.path.join')
    @mock.patch('utils.git_utils.os.path.normpath')
    @mock.patch('utils.git_utils.git_execute')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_untracked_files(self, mock_ope, mock_ge, mock_opn, \
                                 mock_opj, mock_grr):
        mock_ope.return_value = True
        mock_ge.return_value = "1\n"
        mock_opn.return_value = "1"
        mock_opj.return_value = ""
        mock_grr.return_value = ""
        self.assertEqual(["1"], get_untracked_files("blah.txt"))

    @mock.patch('utils.git_utils.os.path.isfile')
    @mock.patch('utils.git_utils.os.path.dirname')
    @mock.patch('utils.git_utils.os.path.normpath')
    @mock.patch('utils.git_utils.git_execute')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_repo_root(self, mock_ope, mock_ge, mock_opn, mock_opd, \
                           mock_opif):
        mock_ope.return_value = True
        mock_ge.return_value = ""
        mock_opn.return_value = "1"
        mock_opd.return_value = ""
        mock_opif.return_value = True
        self.assertEqual("1", get_repo_root("blah.txt"))

    @mock.patch('utils.git_utils.os.path.isfile')
    @mock.patch('utils.git_utils.os.path.dirname')
    @mock.patch('utils.git_utils.git_execute')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_repo_branch(self, mock_ope, mock_ge, mock_opd, mock_opif):
        mock_ope.return_value = True
        mock_ge.return_value = "1"
        mock_opd.return_value = ""
        mock_opif.return_value = True
        self.assertEqual("1", get_repo_branch("blah.txt"))

    @mock.patch('utils.git_utils.os.path.isfile')
    @mock.patch('utils.git_utils.os.path.dirname')
    @mock.patch('utils.git_utils.git_execute')
    @mock.patch('utils.git_utils.os.path.exists')
    def test_get_repo_url(self, mock_ope, mock_ge, mock_opd, mock_opif):
        mock_ope.return_value = True
        mock_ge.return_value = "1"
        mock_opd.return_value = ""
        mock_opif.return_value = True
        self.assertEqual("1", get_repo_url("http://blah.com"))

    @mock.patch('utils.git_utils.subprocess.Popen')
    def test_get_execute_no_params(self, mock_spp):
        mock_spp.return_value = StubForP()
        self.assertEqual("Stubbed", git_execute(""))

class StubForP():
    def communicate(self):
        return ("Stubbed","Error")
